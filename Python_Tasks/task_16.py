numbers = [5, 8, 12, 15, 20]
print("Number of elements in the list numbers is", len(numbers))
print("Sum of elements of the list numbers is", sum(numbers))
for i, number in enumerate(numbers, start=1):
    print(i, number)
fruits = ["Apple", "Banana", "Orange"]
quantities = [3, 5, 2]
for x, y in zip(fruits, quantities):
    print(x, y)
