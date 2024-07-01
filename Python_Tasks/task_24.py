def update_file(new_info):
    with open("my_file.txt", "a") as file:
        file.write(new_info)


with open("my_file.txt", "w") as file:
    file.write("Name: Keerthana S\n")
    file.write("Programming: Python\n")
    file.write("Welcome to the world of Python\n")

with open("my_file.txt", "r") as file:
    initial_content = file.read()
    print("Initial Content: ", initial_content)

update_file("Hello Everyone!!!!")
with open("my_file.txt", "r") as file:
    updated_content = file.read()
    print("Updated Content: ", updated_content)
