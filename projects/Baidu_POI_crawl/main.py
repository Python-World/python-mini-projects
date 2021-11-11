import os
import os.path as osp
from util import *


## ---------- config ----------
# 百度AK
baidu_web_ak = 'your AK'
# 范围(左下点经纬度，右上点经纬度，x经度，y纬度)
wgs_l_x = 105.824149
wgs_l_y = 28.524360
wgs_r_x = 111.659451
wgs_r_y = 31.730663
# 滑动窗口大小(默认0.5效果不错)
kernel_x = 0.5
kernel_y = 0.5
# 索引号
rec_index = 1
# 兴趣区关键字
roi_key = '桥'
# 保存目录
output = 'output'


# # 新建文件夹
# ! mkdir -p output
# 获取百度坐标系下的研究区范围
rec_index -= 1
l_x, l_y = wgs84_to_baidu(wgs_l_x, wgs_l_y, baidu_web_ak)
r_x, r_y = wgs84_to_baidu(wgs_r_x, wgs_r_y, baidu_web_ak)
print('左下点经纬度：', l_x, l_y)
print('右上点经纬度：', r_x, r_y)
num_x = math.ceil((r_x - l_x) / kernel_x)
num_y = math.ceil((r_y - l_y) / kernel_y)
num_rec = num_x * num_y
print('网格数：', num_rec)
for idx in range(rec_index, num_rec):
    rec_str = get_rectangle(l_x, l_y, r_x, r_y, kernel_x, kernel_y, idx)
    print('第', (idx+1), '块网格，当前区域坐标：', rec_str)
    get_baidu_poi(roi_key, rec_str, baidu_web_ak, idx, output)
    print('当前区域完成')
    time.sleep(1)