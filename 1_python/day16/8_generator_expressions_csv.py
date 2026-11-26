import csv

def read_employees(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            salary = int(row['salary'])

            if salary > 50000:
                row['salary'] = salary
                yield row


employees = read_employees("../../docs/employees.csv")
for employee in employees:
    print(employee)
