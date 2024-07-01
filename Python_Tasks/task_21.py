from my_package.module1 import add
from my_package.module2 import multiply
from my_package.sub_package.sub_module1 import subtract
from my_package.sub_package.sub_module2 import divide

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("Addition of 2 numbers = ", add(a, b))
print("Multiplication of 2 numbers = ", multiply(a, b))
print("subtraction of 2 numbers = ", subtract(a, b))
print("Division of 2 numbers = ", divide(a, b))
