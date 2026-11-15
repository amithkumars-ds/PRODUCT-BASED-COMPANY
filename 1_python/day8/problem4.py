from decimal import Decimal

class Employee:
    employee_count = 0 

    def __init__(self, name:str, salary:Decimal):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    def display_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"




if __name__ == "__main__":
    emp1 = Employee("Raj", Decimal("1000.45"))
    emp2 = Employee("Kumar", Decimal("1120.45")
    
    print(emp1.display_info())
    print(emp2.display_info())
    print(Employee.get_employee_count())
