class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: {self.salary}")


class BankAccount:
    def __init__(self, holder_name, acc_number, balance):
        self.holder_name = holder_name
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful.")
        self.display_balance()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
            self.display_balance()
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius**2
        print(f"Area of the circle: {area}")

    def calculate_circumference(self):
        circumference = 2 * 3.14 * self.radius
        print(f"Circumference of the circle: {circumference}")


emp = Employee("Keerthana", 1001, 50000)
emp.display_info()
print()

acc = BankAccount("Keerthu", "123456789", 1000)
acc.deposit(500)
acc.withdraw(200)
print()

circle = Circle(5)
circle.calculate_area()
circle.calculate_circumference()
