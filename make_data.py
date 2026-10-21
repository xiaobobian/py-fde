import csv
result={}


try:
    with open("orders.csv",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.setdefault(row["city"],0)
            # row_count+=1
            result[row["city"]]+=1
    print(result)
except ValueError as e:
    print(e)







