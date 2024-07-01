class Employee:
    company = "Fictional Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Company Name:", Employee.company)


# Creating instances of the Employee class
employee1 = Employee("Keerthana", 50000)
employee2 = Employee("Jyothi", 60000)

# Calling display_info method for each instance
employee1.display_info()
employee2.display_info()

# Updating the company name
Employee.company = "New Fictional Company"

# Creating a new instance
employee3 = Employee("Krish", 55000)

# Calling display_info method for the new instance
employee3.display_info()
