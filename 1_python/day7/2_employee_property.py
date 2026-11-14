class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary should be greater than 0!")
        self._salary = salary



if __name__ == "__main__":
    employee = Employee("Rahul", 50000)

    print(employee.name)
    print(employee.salary)

    employee.salary = 60000
    print(employee.salary)

    try:
        employee.salary = -1000
    except ValueError as e:
        print(e)

    try:
        employee.name = "Amit"
    except AttributeError as e:
        print(e)
