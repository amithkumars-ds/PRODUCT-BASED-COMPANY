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



if __name__ == "__main__":
    emp1 = Employee("Harish", 50000, 101)
    emp2 = Employee("Chandan", 60000, 102)

    emp1.give_raise(5000)

    emp1.display_info()
    emp2.display_info()

    print(f"\nTotal employees: {Employee.employee_count}")
