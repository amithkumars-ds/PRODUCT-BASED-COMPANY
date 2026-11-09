class Employee:
    company = "Google" # class attribute

    def __init__(self, 
                 name: str,
                 salary: int):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")



if __name__ == "__main__":
    emp1 = Employee("Harish", 50000)
    emp1.company = "Microsoft" # change 1st emp company to Microsoft
    
    emp2 = Employee("Chandan", 10000)
    emp2.company = "Meta"
    
    # print company of both the employees
    print(emp1.company)       # Microsoft
    print(emp2.company)       # Google
    print(Employee.company)   # Google

