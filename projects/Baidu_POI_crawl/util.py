import requests
import json
import time
    
    
# call API
def get_baidu_poi(roi_key, city_str, baidu_ak, output):
    """
    inputs:
        roi_key: poi name
        city_str: city name
        baidu_ak: baidu web API AK
        output: file save path
    """
    now_time = time.strftime("%Y-%m-%d")
    page_num = 0
    logfile = open(output + "/" + now_time + ".log", "a+", encoding="utf-8")
    file = open(output + "/" + now_time + ".txt", "a+", encoding="utf-8")
    while True:
        try:
            URL = "http://api.map.baidu.com/place/v2/search?query=" + roi_key + \
                "&region=" + city_str + \
                "&output=json" +  \
                "&ak=" + baidu_ak + \
                "&scope=2" + \
                "&page_size=20" + \
                "&page_num=" + str(page_num)
            resp = requests.get(URL)
            res = json.loads(resp.text)
            if len(res["results"]) == 0:
                logfile.writelines(time.strftime("%Y-%m-%d-%H-%M-%S") + " " + city_str + " " + str(page_num) + "\n")
                break
            else:
                for r in res["results"]:
                    j_name = r["name"]
                    j_lat = r["location"]["lat"]
                    j_lon = r["location"]["lng"]
                    j_area = r["area"]
                    j_add = r["address"]
                    j_str = str(j_name) + "," + str(j_lon) + "," + str(j_lat) + "," + str(j_area) + "," + str(j_add) + "\n"
                    file.writelines(j_str)
            page_num += 1
            time.sleep(1)
        except:
            print("except")
            logfile.writelines(time.strftime("%Y-%m-%d-%H-%M-%S") + " " + city_str + " " + str(page_num) + "\n")
            break