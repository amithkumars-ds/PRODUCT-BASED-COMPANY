class Employee:
    company = "Google" # class attribute: created when class is created
    employee_count = 0 # class attribute

    def __init__(self, name, salary):
        self.name = name # instance attribute
        self.salary = salary # instance attribute
        Employee.employee_count += 1
        



if __name__ == "__main__":
    employee1 = Employee("Harish", 1000) # creating an instance of employee class
    employee2 = Employee("Chandan", 5000) # creating an instance of employee class
    employee3 = Employee("Rakesh", 4000) # creating an instance of employee class

    print(employee3.employee_count)
