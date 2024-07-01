def greet_user():       #prints greeting message
    print("Hello! Welcome!")
def print_numbers():       #prints numbers from 1 to 5
    for num in range(1,6):
        print(num)
def print_pattern():    #prints the pattern
    for i in range(1,6):
        for j in range(0,i):
            print('*',end="")
        print("\n")
def print_table():      #prints the multiplication table of 2
    for i in range(1,11):
        for j in range(1,2):    #Nested loop just for 2
            print(f'{2} * {i} = {i*j}')

greet_user()
print("printing numbers..")
print_numbers()

print("Printing pattern: ")
print_pattern()

print("Printing Multiplication table of 2: ")
print_table()