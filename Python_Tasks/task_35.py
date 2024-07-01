# Define a lambda function named `square` that takes a parameter `x` and returns the square of `x`.
square = lambda x: x**2

# Define a lambda function named `multiply` that takes two parameters `a` and `b` and returns their product.
multiply = lambda a, b: a * b

# Create a file named `example.txt` and write some text to it.
with open("example.txt", "w") as f:
    f.write("Welcome To Python Programming.\n")

# Use the `with` statement to open the file `example.txt` in read mode and print its contents.
with open("example.txt", "r") as f:
    print("Contents of example.txt:")
    print(f.read())

# Use the `with` statement to open the file `example.txt` in write mode and append some additional text to it.
with open("example.txt", "a") as f:
    f.write("This is Keerthana Here.")
