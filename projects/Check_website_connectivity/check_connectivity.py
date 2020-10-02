import csv

import requests


status_dict = {"Website": "Status"}


def main():
    with open("websites.txt", "r") as fr:
        for line in fr:
            website = line.strip()
            status = requests.get(website).status_code
            status_dict[website] = "working" if status == 200 \
                else "not working"

    # print(status_dict)
    with open("website_status.csv", "w", newline="") as fw:
        csv_writers = csv.writer(fw)
        for key in status_dict.keys():
            csv_writers.writerow([key, status_dict[key]])


if __name__ == "__main__":
    main()
