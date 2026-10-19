import csv
with open("orders.csv",encoding="utf-8") as f:
    row_count = 0
    reader = csv.DictReader(f)
    for row in reader:
      #  print(row['customer'],row['city'])
        row_count=row_count+1
#    print(row_count)
file="orders_1000.csv"
try:
    with open(file,encoding="utf-8") as f:
       # amount=0
        customer={}
        error=0
        #customer.setdefault(error, 0)
        reader = csv.DictReader (f)
        for row in reader:
            customer.setdefault(row["customer"],0)
            try:
                customer[row["customer"]]+=int(row["amount"])
            except ValueError:
                error+=1
except FileNotFoundError as e:
    print(e)


with open("summary.csv","w", encoding="utf-8", newline='') as f:
        csv.writer(f).writerow(["我的表格标题"])
        writer = csv.DictWriter(f, fieldnames=["customer", "amount"])
        writer.writeheader()

        for row,rowvalue in customer.items():
            writer.writerow({"customer":str(row),"amount":int(rowvalue)})









