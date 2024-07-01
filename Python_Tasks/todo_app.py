class TodoItem:
    count = 1

    def __init__(self, todo, is_completed):
        self.id = TodoItem.count
        self.todo = todo
        self.is_completed = is_completed
        TodoItem.count += 1

    def __str__(self):
        if self.is_completed:
            return f"[X] {self.todo}"
        return f"[] {self.todo}"


class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def mark_completed(self, id):
        for todo in self.todos:
            if todo.id == id:
                todo.is_completed = True
                break

    def display_todos(self):
        for todo in self.todos:
            print(f"{todo.id} {todo}")

    def save(self):
        with open("todos.txt", "w") as file:
            for todo in self.todos:
                file.write(f"{todo.todo},{todo.is_completed}\n")

    # todo_list = TodoList()
    # todo_item1 = TodoItem("Buy Milk", False)
    # todo_item2 = TodoItem("Study", False)

    # todo_list.add_todo(todo_item1)
    # todo_list.add_todo(todo_item2)
    # todo_list.display_todos()
    # todo_list.save()

    def load(self):
        with open("todos.txt", "r") as file:
            for line in file.readlines():
                todo, is_completed = line.strip().split(",")
                todo_item = TodoItem(todo, is_completed == "True")
                self.add_todo(todo_item)


# todo_list = TodoList()
# todo_list.load()
# todo_list.display_todos()


class TodoApp:
    def run(self):
        todo_list = TodoList()
        while True:
            print("TodoApp")
            print("1-Add Todo")
            print("2-Mark Completed")
            print("3-Display Todos")
            print("4-Save")
            print("5-Load")
            print("6-Exit")
            option = input("Enter option {1-6}:")
            if option == "1":
                todo = input("Enter todo:")
                todo_item = TodoItem(todo, False)
                todo_list.add_todo(todo_item)
            elif option == "2":
                id = int(input("Enter id: "))
                todo_list.mark_completed(id)
            elif option == "3":
                todo_list.display_todos()
            elif option == "4":
                todo_list.save()
            elif option == "5":
                todo_list.load()
            elif option == "6":
                break
            else:
                print("Invalid Option")


app = TodoApp()
app.run()
