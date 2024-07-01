from my_package import *
from my_package.sub_package import *

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("Addition of 2 numbers = ", module1.add(a, b))
print("Multiplication of 2 numbers = ", module2.multiply(a, b))
print("subtraction of 2 numbers = ", sub_module1.subtract(a, b))
print("Division of 2 numbers = ", sub_module2.divide(a, b))
