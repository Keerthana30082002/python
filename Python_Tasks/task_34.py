class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            return "Error.Division by zero is not allowed."
        else:
            return result


calc = Calculator()  # creating instances of calculator class
# Testing each method with different inputs
print("Addition:", calc.add(5, 3))
print("Subtraction:", calc.subtract(5, 3))
print("Multiplication:", calc.multiply(5, 3))
print("Division(valid input):", calc.divide(6, 3))
print("Division(invalid input):", calc.divide(6, 0))
