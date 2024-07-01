class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


student_values = Student("Keerthana", 21, "A+")
book_values = Book("Python programming", "Jane Smith", 500)
# printing Student details
print(f"Name: {student_values.name}")
print(f"Age: {student_values.age}")
print(f"Grade: {student_values.grade}")
# printing book details
print(f"Book Title: {book_values.title}")
print(f"Book author: {book_values.author}")
print(f"Book Price: {book_values.price}")
