import json
from stats import sum_by_customer
result=sum_by_customer("orders.csv")
first=result[0]
second=result[1]
with open("customer_totals.json","w",encoding="utf-8") as f:
        try:
            json.dump(first,f,indent=4)

        except Exception as e:
            print(e)
json_file=open("customer_totals.json","r",encoding="utf-8")
json_data=json.load(json_file)
print(json_data)
json_file.close()

print(second)

print(json_data==first)




