import requests
import csv

status_dict = {"Website": "Status"}

if __name__ == "__main__":

    with open("websites.txt", "r") as fr:
        for line in fr:
            status = requests.get(line.strip()).status_code
            status_dict[line] = "working" if status == 200 else "not working"

    print(status_dict)
    with open("website_status.csv", "w", newline="") as fw:
        csv_writers = csv.writer(fw)
        for key in status_dict.keys():
            csv_writers.writerow([key, status_dict[key]])
