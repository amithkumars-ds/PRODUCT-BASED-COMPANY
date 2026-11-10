class Employee:
    company = "Google"
    employee_count = 0

    def __init__(self,
                 name,
                 salary,
                 employee_id):
        self.name = name
        self.salary = salary
        self.employee_id = employee_id
        Employee.employee_count += 1


    def display_info(self):
        print("\nEmployee Details")
        print("-"*50)
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Salary: {self.salary}")
        print(f"Employee ID: {self.employee_id}")

    def give_raise(self, increment):
        self.salary += increment
    
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0



if __name__ == "__main__":
    emp1 = Employee("Harish", 50000, 101)
    emp2 = Employee("Chandan", 60000, 102)

    emp1.give_raise(5000)

    emp1.display_info()
    emp2.display_info()

    print("\n")
    print(Employee.get_employee_count())
    print(Employee.is_valid_salary(50000))
    print(Employee.is_valid_salary(-100))
