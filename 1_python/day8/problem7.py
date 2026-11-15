class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def display_person(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name:str, age:int, employee_id:str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee(self):
        person_details = super().display_person()
        return f"{person_details}, Employee ID: {self.employee_id}"

class Manager(Employee):
    def __init__(self, name:str, age:int, employee_id:str,
                 department:str):
        super().__init__(name, age, employee_id)
        self.department = department

    def display_manager(self):
        employee_details = super().display_employee()
        return f"{employee_details}, Department: {self.department}"





if __name__ == "__main__":
    # Test Person
    person = Person("Raj", 30)
    print(person.display_person())

    # Test Employee
    employee = Employee("Kumar", 28, "EMP101")
    print(employee.display_person())
    print(employee.display_employee())

    # Test Manager
    manager = Manager("Arun", 35, "MGR101", "Engineering")
    print(manager.display_person())
    print(manager.display_employee())
    print(manager.display_manager())


