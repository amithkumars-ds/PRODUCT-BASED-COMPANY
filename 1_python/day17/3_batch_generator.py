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

def generate_batch(filtered_rows, batch_size=1000):
    batch = []
    for row in filtered_rows:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch
     



if __name__ == "__main__":
    raw_rows = read_csv("../../docs/employees.csv")
    transformed_rows = transform_salary(raw_rows)
    filtered_rows = filter_employees(transformed_rows, 50000)
    batched_rows = generate_batch(filtered_rows, batch_size=2)

    for row in batched_rows:
        print(row)
