import os

class TodoItem:
    count = 0

    def __init__(self, todo, is_completed=False):
        TodoItem.count += 1
        self.id = TodoItem.count
        self.todo = todo
        self.is_completed = is_completed

    def __str__(self):
        status = " [x] " if self.is_completed else " [ ] "
        return f"{self.id}. {status}{self.todo}"

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def mark_completed(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.is_completed = True
                return True
        return False

    def display_todos(self):
        for todo in self.todos:
            print(todo)

    def save(self, filename):
        with open(filename, 'w') as file:
            for todo in self.todos:
                file.write(f"{todo.id},{todo.todo},{todo.is_completed}\n")

    def load(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    todo_id, todo, is_completed = line.strip().split(',')
                    self.add_todo(TodoItem(todo, is_completed == 'True'))

class TodoApp:
    def __init__(self):
        self.todo_list = TodoList()

    def run(self):
        menu = (
            "1. Add Todo\n"
            "2. Mark Completed\n"
            "3. Display Todos\n"
            "4. Save\n"
            "5. Load\n"
            "6. Exit\n"
        )

        while True:
            print("Todo App Menu:")
            print(menu)
            choice = input("Enter your choice: ")

            if choice == '1':
                todo = input("Enter the todo: ")
                self.todo_list.add_todo(TodoItem(todo))
            elif choice == '2':
                todo_id = int(input("Enter the ID of the todo to mark as completed: "))
                if not self.todo_list.mark_completed(todo_id):
                    print("Todo not found!")
            elif choice == '3':
                print("Todos:")
                self.todo_list.display_todos()
            elif choice == '4':
                filename = input("Enter the filename to save: ")
                self.todo_list.save(filename)
                print("Todo list saved successfully!")
            elif choice == '5':
                filename = input("Enter the filename to load: ")
                self.todo_list.load(filename)
                print("Todo list loaded successfully!")
            elif choice == '6':
                print("Exiting Todo App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_app = TodoApp()
    todo_app.run()
