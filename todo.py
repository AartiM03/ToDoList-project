#An empty list to store the tasks
tasks = []

#Function to add tasks to the list
def add_task():
    task = input("Enter the task description: ")
    priority = input("Enter the task priority (high, medium, low): ")
    tasks.append({"description": task, "priority": priority})
    print("Task added successfully!")

#Function to display the task list
def show_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Task List:")
        for index,task in enumerate(tasks):
            print(f"{index+1}. {task['description']} (Priority: {task['priority']})")

#Function to remove a task or mark it as completed
def complete_task():
    if len(tasks) == 0:
        print("No tasks found.")
        return
    
    show_tasks()
    index = int(input("Enter the index of the task to mark as cmpleted or remove: "))

    if index<0 or index >= len(tasks):
        print("Invalid index.")
    else:
        task = tasks[index]
        choice = input(f"Do you want to mark '{task['description']}' as completed? (Y/N): ")
        if choice.lower() == "y":
            tasks.pop(index)
            print("Task marked as completed and removed from the list.")
        else:
            print("Action canceled.")

#Sorting the tasks
def sort_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
        return
    
    print("Sort Options:")
    print("1. Sort by priority")
    print("2. Sort by description")
    print("3. Cancel")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        tasks.sort(key=lambda x: x["priority"])
        print("Tasks sorted by priority.")
    elif choice == "2":
        tasks.sort(key=lambda x: x["description"])
        print("Tasks sorted by description.")
    elif choice == "3":
        print("Sorting canceled.")
    else:
        print("Invalid choice. Please try again.")


#A loop to continuously prompt the user for actions until they choose to exit.
while True:
    print("\nTodo List Application")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task as completed or remove")
    print("4. Sort tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        sort_tasks()
    elif choice == "5":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")
