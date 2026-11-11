class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        return f"Name: {self.name}, Age: {self.age}"


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee(self):
        name_age = super().display_person()
        return f"{name_age}, Employee ID: {self.employee_id}"

class Manager(Employee):
    def __init__(self, name, age, 
                 employee_id,
                 department):
        super().__init__(name, age, employee_id)
        self.department = department

    def display_manager(self):
        name_age_eid = super().display_person()
        return f"{name_age_eid}, Department: {self.department}"




if __name__ == "__main__":
    manager = Manager("Rahul", 35, "EMP101", "Engineering")

    print(manager.display_person())
    print(manager.display_employee())
    print(manager.display_manager())
