import csv

filename = "data.csv" # on windows you may have to use this format: "C:\\Users\<username>\<git_reponame>\work-with-csv\data.csv"
# csv content
# priority;name;ip;os

def list_all_item():
    print("1. get all data:")
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            print(lines)
    print("\n")

def sum_the_rows():
    print("2. count the rows")
    input_file = open(filename,"r+")
    reader_file = csv.reader(input_file)
    value = len(list(reader_file))

    print(f'Row count {value}')
    print("\n")

def get_priority_min_max():
    print("3. list the minimum and the maximum priority number")
    with open(filename, "r") as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        minVal, maxVal = [], []
        for i in data:
            minVal.append(i[0])
            maxVal.append(i[0])

    print(f'Row min {min(minVal)}')
    print(f'Row max {max(maxVal)}')
    print("\n")

def main():
    list_all_item()
    sum_the_rows()
    get_priority_min_max()

if __name__ == "__main__":
   main()