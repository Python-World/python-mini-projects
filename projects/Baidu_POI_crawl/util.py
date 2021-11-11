from urllib.request import urlopen, quote
import requests
import json
import time
import math


# WGS84转Baidu坐标系
def wgs84_to_baidu(x, y, baidu_ak):
    '''
    inputs:
        x: WGS84下的经度
        y: WGS84下的纬度
        baidu_ak: 百度web API的AK秘钥
    outputs:
        tuple: 百度坐标系下的经纬度
    '''
    data = str(x) + ',' + str(y)
    url = 'http://api.map.baidu.com/geoconv/v1/?coords=' + data + '&from=1&to=5&ak=' + baidu_ak
    req = urlopen(url)
    res = req.read().decode()
    temp = json.loads(res)
    baidu_x = 0
    baidu_y = 0
    if temp['status'] == 0:
        baidu_x = temp['result'][0]['x']
        baidu_y = temp['result'][0]['y']
    else:
        print(temp['message'])
    return (baidu_x, baidu_y)
    
    
# 获取当前小范围区域
def get_rectangle(l_x, l_y, r_x, r_y, kernel_x, kernel_y, index):
    '''
    inputs:
        l_x: 百度坐标系下的左下角点经度
        l_y: 百度坐标系下的左下角点纬度
        r_x: 百度坐标系下的右上角点经度
        r_y: 百度坐标系下的右上角点纬度
        kernel_x: 经度方向核大小
        kernel_y: 纬度方向核大小
        index: 当前位置索引
    outputs:
        string: 用于API的滑动窗口范围(左下右上模式)
    '''
    num_x = math.ceil((r_x - l_x) / kernel_x)
    num_y = math.ceil((r_y - l_y) / kernel_y)
    left_x = l_x + kernel_x * (index % num_x)
    left_y = l_y + kernel_y * (index // num_x)
    right_x = (left_x + kernel_x)
    right_y = (left_y + kernel_y)
    rec_str = str(left_y) + ',' + str(left_x) + ',' + str(right_y) + ',' + str(right_x)  # 这里返回是纬度，经度，要符合百度的API要求
    return rec_str
    
    
# Baidu系坐标到WGS84
x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方


def bd09_to_gcj02(bd_lon, bd_lat):
    '''
    inputs:
        bd_lat: 百度坐标纬度
        bd_lon: 百度坐标经度
        return: 转换后的坐标列表形式
    '''
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]


def gcj02_to_wgs84(lng, lat):
    '''
    inputs:
        lng: 火星坐标系经度
        lat: 火星坐标系纬度
        return: 转换后的坐标列表形式
    '''
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)


def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret
 

def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


# 判断是否在国内，不在国内不做偏移
def out_of_china(lng, lat):
    '''
    inputs:
        lng: 火星坐标系经度
        lat: 火星坐标系纬度
        return: 转换后坐标
    '''
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)
    
    
# 对小窗口调用百度API
def get_baidu_poi(roi_key, rec_str, baidu_ak, index, output):
    '''
    inputs:
        roi_key: 兴趣区关键字
        rec_str: 滑动小区域坐标
        baidu_ak: 百度web API的AK秘钥
        index: 滑动小窗索引
        output: 文件保存位置
    '''
    now_time = time.strftime("%Y-%m-%d")
    page_num = 0
    logfile = open(output + '/' + now_time + ".log", 'a+', encoding='utf-8')
    file = open(output + '/' + now_time + ".txt", 'a+', encoding='utf-8')
    while True:
        try:
            URL = "http://api.map.baidu.com/place/v2/search?query=" + roi_key + \
                "&bounds=" + rec_str + \
                "&output=json" +  \
                "&ak=" + baidu_ak + \
                "&scope=2" + \
                "&page_size=20" + \
                "&page_num=" + str(page_num)
            resp = requests.get(URL)
            res = json.loads(resp.text)
            # print('获取兴趣区')
            if len(res['results']) == 0:
                logfile.writelines(time.strftime("%Y-%m-%d-%H-%M-%S") + " stop " + str(index) + " " + rec_str + " " + str(page_num) + '\n')
                break
            else:
                for r in res['results']:
                    j_name = r['name']  # 获取名称
                    # 获取经纬度
                    j_lat = r['location']['lat']
                    j_lon = r['location']['lng']
                    j_area = r['area']  # 获取行政区
                    j_add = r['address']  # 获取具体地址
                    j_lon, j_lat = bd09_to_wgs84(j_lon, j_lat)  # 坐标转换
                    j_str = str(j_name) + ',' + str(j_lon) + ',' + str(j_lat) + ',' + str(j_area) + ',' + str(j_add) + '\n'
                    file.writelines(j_str)
            page_num += 1
            time.sleep(1)
        except:
            print("except")
            logfile.writelines(time.strftime("%Y-%m-%d-%H-%M-%S") + " except "  + str(index) + " " + rec_str + " " + str(page_num) + '\n')
            break