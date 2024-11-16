class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def mark_uncompleted(self):
        self.completed = False

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.description}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_file()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def edit_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
            self.save_to_file()
        else:
            print("Invalid task index!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_to_file()
        else:
            print("Invalid task index!")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_to_file()
        else:
            print("Invalid task index!")

    def mark_uncompleted(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_uncompleted()
            self.save_to_file()
        else:
            print("Invalid task index!")

    def save_to_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.completed}\n")

    def load_from_file(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    description, completed = line.strip().split(',')
                    self.tasks.append(Task(description, completed == 'True'))
        except FileNotFoundError:
            print("tasks.txt not found, starting fresh!")


def main():
    todo_list = TodoList()
    todo_list.load_from_file()

    while True:
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Edit an existing task")
        print("4. Delete a task")
        print("5. Mark a task as completed")
        print("6. Mark a task as uncompleted")
        print("7. Exit")
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            description = input("Enter task description: ")
            new_task = Task(description)
            todo_list.add_task(new_task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to edit: ")) - 1
                new_description = input("Enter new task description: ")
                todo_list.edit_task(index, new_description)
            except ValueError:
                print("Invalid input!")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo_list.delete_task(index)
            except ValueError:
                print("Invalid input!")
        elif choice == '5':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                todo_list.mark_completed(index)
            except ValueError:
                print("Invalid input!")
        elif choice == '6':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to mark as uncompleted: ")) - 1
                todo_list.mark_uncompleted(index)
            except ValueError:
                print("Invalid input!")
        elif choice == '7':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Please enter a valid number.")

if __name__ == "__main__":
    main()

