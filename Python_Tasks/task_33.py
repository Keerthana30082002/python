class Employee:
    raise_percentage = 0.05  # Default raise percentage

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary *= 1 + self.raise_percentage / 100

    @classmethod
    def set_raise_percentage(cls, percentage):
        cls.raise_percentage = percentage


# Creating instances of the Employee class
emp1 = Employee("Keerthu", 50000)
emp2 = Employee("Krish", 60000)

# Observing salary increase based on default raise percentage
print("Before raise:")
print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)

emp1.apply_raise()
emp2.apply_raise()

print("After raise:")
print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)

# Changing raise percentage
Employee.set_raise_percentage(7)

# Creating a new instance to observe the effect of updated raise percentage
emp3 = Employee("Jyothi", 55000)

print("Before raise with updated percentage:")
print(emp3.name, emp3.salary)

emp3.apply_raise()

print("After raise with updated percentage:")
print(emp3.name, emp3.salary)
