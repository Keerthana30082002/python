class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Person: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print(
            f"Book: {self.title}, Author: {self.author}, Year: {self.publication_year}"
        )


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print(f"Rectangle Area: {area}")

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(f"Rectangle Perimeter: {perimeter}")


person = Person("Keerthana", 21, "Female")
person.display_info()

book = Book("Five point someone", "chetan bhagat", 2000)
book.display_info()

rectangle = Rectangle(3, 4)
rectangle.calculate_area()
rectangle.calculate_perimeter()
