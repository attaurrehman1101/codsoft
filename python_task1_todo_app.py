# codsoft
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def list_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Not Done"
            print(f"{index}. {task.description} - {status}")

    def mark_task_as_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
        else:
            print("Invalid task index.")

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]

def main():
    todo_list = ToDoList()

    while True:
        print("===== To-Do List =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_as_completed(task_index)
        elif choice == "4":
            todo_list.remove_completed_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
