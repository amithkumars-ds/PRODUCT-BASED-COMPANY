class Employee:
    def __init__(self,
                  name,
                  salary):
         self.name = name
         self.salary = salary

    def display_info(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self,
                 name,
                 salary,
                 department):
        super().__init__(name, salary)
        self.department = department


    def display_info(self):
        name_salary = super().display_info()
        return f"{name_salary}, Department: {self.department}"



if __name__ == "__main__":
    emp = Employee("Rahul", 50000)
    manager = Manager("Priya", 90000, "Engineering")

    print(emp.display_info())
    print(manager.display_info())
