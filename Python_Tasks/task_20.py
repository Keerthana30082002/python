from my_module1 import square
from my_module2 import cube

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    sq = square(i)
    c = cube(i)
    print(f"Square of {i} = {sq}")
    print(f"Cube of {i} = {c}")
