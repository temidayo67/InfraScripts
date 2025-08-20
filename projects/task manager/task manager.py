class Task:
    category= "General"  # Default category for all tasks
    def __init__(self, description, cost):
        self.description = description  # Task description
        self.cost = cost  # Task cost
    def __str__(self):
        # String representation of a task
        return f"Description: {self.description}, Cost: ${self.cost}"
    @staticmethod
    def info():
        # Static method for general info about tasks
        return "Tasks track work and cost."

class TaskManager(Task):
    def __init__(self):
        # Initialize as a Task, then set up task list and budget
        super().__init__("Manager", 0)
        self.tasks = []  # List to store Task objects
        self.budget = {"work": 1000, "personal": 500}  # Budget by category
    @property
    def total_cost(self):
        # Total cost of all tasks
        return sum(task.cost for task in self.tasks)
    @classmethod
    def get_category(cls):
        # Get the default category
        return cls.category
    def add_task(self, description, cost, category):
        # Add a new task and update budget
        try:
            cost= float(cost)
            if cost > 0 and description:
                self.tasks.append(Task(description, cost))
                self.budget[category] -= cost
                return f"Added: {description}"
            return "Invalid Input"
        except ValueError:
            return "Cost must be a number."
    def remove_task(self, index):
        # Remove a task by index
        try:
            task= self.tasks.pop(index)
            return f"Removed: {task}"
        except IndexError:
            return "Invalid index!"
    def view_tasks(self):
        # View all tasks and total cost
        result= f"Tasks (Total Cost: ${self.total_cost:.2f}):\n"
        for i, task in enumerate(self.tasks):
            result += f"{i}: {task}\n"
        return result
    def __str__(self):
        # String representation of the manager
        return f"Task Manager - Budget: {self.budget}"

def main():
    manager = TaskManager()  # Create a TaskManager instance
    global category
    category = manager.get_category()
    while True:
        print("\n1: Add Task, 2: Remove Task, 3: View Tasks, 4: Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            desc = input("Task description: ")
            cost = input("Task cost: ")
            cat = input("Category (Work/Personal): ")
            print(manager.add_task(desc, cost, cat))
        elif choice == "2":
            index = int(input("Task index to remove: "))
            print(manager.remove_task(index))
        elif choice == "3":
            print(manager.view_tasks())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
    print(f"Final Budget: {manager.budget}")

if __name__ == "__main__":
    desc, cost = "Sample Task", 50.0
    print(f"Starting with {desc}: ${cost}")

    main()
