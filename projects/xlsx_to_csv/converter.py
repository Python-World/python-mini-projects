import xlrd
import csv
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('--xlsx', required=True)
argparser.add_argument('--csv', required=True)


def csv_from_excel():
    args = argparser.parse_args()
    wb = xlrd.open_workbook(args.xlsx)
    sh = wb.sheet_by_index(0)
    with open(args.csv, 'w') as your_csv_file:
        wr = csv.writer(your_csv_file)
        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))


if __name__ == '__main__':
    csv_from_excel()

