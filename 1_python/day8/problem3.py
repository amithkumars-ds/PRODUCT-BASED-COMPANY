class Student:
    school = "ABC School"

    def __init__(self, name:str, grade:str):
        self.name = name
        self.grade = grade

    def display_info(self):
        return f"Student Name: {self.name}, Grade: {self.grade}, School: {self.school}"


if __name__ == "__main__":
    student1 = Student("Raj", "A")
    student2 = Student("Kumar", "A+")

    student1.school = "MES"
    print(student1.school)

    Student.school = "XYZ School" 

    print(student1.display_info())
    print(student2.display_info())
