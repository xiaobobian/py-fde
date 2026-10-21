import csv


def count_by_city(filename):
    result={}
    with open(filename ,encoding="utf-8" ) as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.setdefault(row["city"],0)
            result[row["city"]]+=1

    return result

if __name__ == "__main__":
    print(count_by_city("orders.csv"))


# print([n*n*n for n in range(1,11) if n%2!=0])