import csv

def read_csv(path):
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def transform_salary(raw_rows):
    for row in raw_rows:
        row["salary"] = int(row["salary"])
        yield row

def filter_employees(transformed_rows, threshold=50000):
    for row in transformed_rows:
        if row["salary"] > threshold:
            yield row



if __name__ == "__main__":
    raw_rows = read_csv("../../docs/employees.csv")
    transformed_rows = transform_salary(raw_rows)
    filtered_rows = filter_employees(transformed_rows, 50000)

    for row in filtered_rows:
        print(row)
