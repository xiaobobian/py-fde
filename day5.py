import json


from stats import count_by_city
result=count_by_city('orders.csv')
with open("city_stats.json","w",encoding="utf-8") as f:
    json.dump(result,f,indent=4,ensure_ascii=False)

with open("city_stats.json","r",encoding="utf-8") as f:
       loaad=json.load(f)


print(result == loaad)
print(result is loaad)