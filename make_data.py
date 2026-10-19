import random

cities = ["Xian", "Beijing", "Shanghai"]
names = ["Tom", "Amy", "Lucy", "Jack"]
statuses = ["paid", "pending", "refunded"]

with open("orders_1000.csv", "w", encoding="utf-8") as f:
    f.write("order_id,customer,city,amount,status\n")
    for i in range(1000):
        f.write(f"{1001 + i},{random.choice(names)},{random.choice(cities)},{random.randint(10, 300)},{random.choice(statuses)}\n")