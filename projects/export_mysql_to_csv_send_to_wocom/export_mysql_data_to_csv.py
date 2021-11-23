# -*- coding: utf-8 -*-
import codecs
import configparser
import csv
import time

import pymysql
import requests as requests

ini = configparser.ConfigParser()
ini.read('config.ini')
wecom_key = ini.get('wecom', 'key')


def sql(sqlstr):  # 定义一个执行SQL的函数
    conn = pymysql.connect(host=ini.get('db', 'host'), user=ini.get('db', 'username'),
                           password=ini.get('db', 'password'), database=ini.get('db', 'database'))
    cursor = conn.cursor()
    cursor.execute(sqlstr)
    results = cursor.fetchall()  # 获取查询的所有记录
    cursor.close()
    conn.close()
    return results


def read_mysql_to_csv(filename):
    with codecs.open(filename=filename, mode='w', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        results = sql(
            ini.get('message', 'sql')
        )
        for result in results:
            write.writerow(result)


def upload_file_robots(filename):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=%(key)s&type=file" % {"key": wecom_key}
    data = {'file': open(filename, 'rb')}  # post jason
    response = requests.post(url=url, files=data)  # post 请求上传文件
    json_res = response.json()  # 返回转为json
    media_id = json_res['media_id']  # 提取返回ID
    return media_id  # 返回请求状态


def send_file_robots(media_id):
    wx_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%(key)s' % {"key": wecom_key}
    data = {"msgtype": "file",
            "file": {"media_id": media_id}}  # post json
    r = requests.post(url=wx_url, json=data)
    return r


if __name__ == '__main__':
    filename = ini.get('message', 'title') + time.strftime('%y%m%d') + '.csv'
    read_mysql_to_csv(filename)
    print(send_file_robots(upload_file_robots(filename)))
