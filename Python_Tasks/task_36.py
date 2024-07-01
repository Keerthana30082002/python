# Create a list of numbers from 1 to 10
numbers = [i for i in range(1, 11)]

# Create a list of squares of numbers
squares = [x**2 for x in numbers]

# Create a list of even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# Create a dictionary of student grades
grades = {"Anu": 70, "Manu": 80, "Raju": 55, "Keerthu": 90, "Annie": 65}

# Create a dictionary of passing grades
passing_grades = {key: value for key, value in grades.items() if value >= 60}

# Increase all grades by 5
grades1 = {key: value + 5 for key, value in grades.items()}

# Create a list of words
words = ["hello", "world", "python", "list", "comprehension"]

# Create a list of lengths of words
lengths = [len(word) for word in words]

print("Original Numbers:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Grades:", grades)
print("Passing Grades:", passing_grades)
print("Increased Grades:", grades1)
print("Words List:", words)
print("Lengths of Words:", lengths)
