from decimal import Decimal
class Employee:
    company = "Google"

    def __init__(self, name:str, salary:Decimal):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Employee: {self.name}, Salary: {self.salary}, Company: {Employee.company}"



if __name__ == "__main__":
    employee1 = Employee("Raj", "10000.45")
    employee2 = Employee("Kumar", "9800.99")

    Employee.company = "Meta"
    print(employee1.display_info())
    print(employee2.display_info())
