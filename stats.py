import csv


def count_by_city(filename):
    result = {}
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.setdefault(row["city"], 0)
            result[row["city"]] += 1

    return result


def sum_by_customer(filename):
    new_result = {}
    error_count = 0
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            new_result.setdefault(row["customer"], 0)
            try:
                new_result[row["customer"]] += int(row["amount"])
            except ValueError:

                error_count += 1

    return new_result, error_count


if __name__ == "__main__":
    print(count_by_city("orders.csv"))
