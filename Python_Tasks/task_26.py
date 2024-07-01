class Student:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.grade = ""


student1 = Student()
student1.name = "Keerthana"
student1.age = 21
student1.grade = "A+"
student2 = Student()
student2.name = "Anu"
student2.age = 22
student2.grade = "A"
student3 = Student()
student3.name = input("Enter the name of the third Student: ")
student3.age = input("Enter the age of the third Student: ")
student3.grade = input("Enter the grade of the third Student: ")

# printing information
print("Student 1: ")
print(f"Name : {student1.name}")
print(f"Age : {student1.age}")
print(f"Grade : {student1.grade}")

print("Student 2: ")
print(f"Name : {student2.name}")
print(f"Age : {student2.age}")
print(f"Grade : {student2.grade}")

print("Student 3: ")
print(f"Name : {student3.name}")
print(f"Age : {student3.age}")
print(f"Grade : {student3.grade}")
