class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return (
            f"Book: {self.title} by {self.author}, Published: {self.publication_year}"
        )


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Rectangle: Length={self.length}, Width={self.width}"


# Creating instances of each class
person = Person("Keerthana", 21, "Female")
book = Book("Python Programming", "Guido van Rossum", 2000)
rectangle = Rectangle(5, 10)

# Printing instances
print(person)
print(book)
print(rectangle)
