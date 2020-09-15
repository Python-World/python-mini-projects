# !/usr/bin/env python
from selenium import webdriver
import json
import requests


# article url
# URL = "https://www.geeksforgeeks.org/what-can-i-do-with-python/"


def download_article(URL):
    # chrome options settings
    chrome_options = webdriver.ChromeOptions()
    settings = {
        "recentDestinations": [
            {"id": "Save as PDF", "origin": "local", "account": ""}
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
    }
    prefs = {
        "printing.print_preview_sticky_settings.appState": json.dumps(settings)
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--kiosk-printing")
    chrome_options.binary_location = (
        r"C:\Program Files (x86)/"
        + r"BraveSoftware\Brave-Browser\Application\brave.exe"
    )
    CHROMEDRIVER_PATH = r"chromedriver.exe"

    # launch browser with predefined settings
    browser = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, options=chrome_options
    )
    browser.get(URL)

    # launch print and save as pdf
    browser.execute_script("window.print();")
    browser.close()


if __name__ == "__main__":
    URL = input("provide article URL: ")
    if requests.get(URL).status_code == 200:
        download_article(URL)
        print("Your article is successfully downloaded")
    else:
        print("Enter a valid  working URL")
