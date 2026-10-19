import csv


with open("orders.csv",encoding="utf-8") as f:
    row_count=0
    data_count=0
    for line in f:
        if row_count != 0:
            print(line.strip())
            data_count += 1
        row_count = row_count + 1
    print(data_count)
    print(row_count)
