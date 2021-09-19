from selenium import webdriver
import requests as rq
import os
from bs4 import BeautifulSoup
import time

path = "D:/webdriver/bin/chromedriver.exe"
url = input("Enter URL:")
output = "nature"

def get_url(path,url):
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    print("loading...")
    res = driver.execute_script("return document.documentElement.outerHTML")
    print("Got page Complete!")
    return res

def get_img_links(res):
    soup = BeautifulSoup(res,"lxml")
    imglinks = soup.find_all("img",src=True)
    print("Get links Complete!")
    return imglinks

def download_img(imglink,index):
    try:
        if "http" not in imglink:
            imglink = "http:" + imglink

        extensions = [".jpg",".jpeg",".png",".gif"]
        extension = ""
        for exe in extensions:
            if imglink.find(exe):
                extension = exe
                break

        img_data = rq.get(imglink).content
        with open(output + "/" + str(index + 1) + extension, "wb+") as f:
            f.write(img_data)
            f.close()
    # get error
    except Exception as e:
        print("False type:",e.__class__.__name__)
        print("False:",e)

res = get_url(path,url)
time.sleep(60)
imglinks = get_img_links(res)

if not os.path.isdir(output):
    os.mkdir(output)

for index, img_link in enumerate(imglinks):
    imglink = img_link["src"]
    print("Downloading...")
    if imglink:
        download_img(imglink, index)

print("Download Complete!")
