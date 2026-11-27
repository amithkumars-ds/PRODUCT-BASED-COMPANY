import csv

# Stage I: CSV Reader
def read_csv(path:str) -> dict:
    with open(path) as file:
        reader = csv.DictReader(file)

        salary_threshold = 50000

        for row in reader:
            row["salary"] = int(row["salary"]) # Stage II: Salary Transformer
            if row["salary"] > salary_threshold: # Stage III: Yield only employees above 50000
                yield row


r = read_csv("../../docs/employees.csv")
for row in r:
    print(row)


