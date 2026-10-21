import csv
# try:
#     int("abc")
# except ValueError:
#     print("数值类型错误")


def count_rows(n):
    num=0
    with open(n,"r",encoding="utf-8") as f:
        for row in csv.DictReader(f):
            num+=1
    return num

print(count_rows("orders_1000.csv"))