tasks = []

def add_task(tasks):
    task = input("Enter tasks: ").strip()
    if not task:
        print("Vacant spaces are not allowed")
        return 

    tasks.append(
        {
            "task": task,
            "completed": "N"
        }
    )

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return 

    for index, task in enumerate(tasks,start=1):
        print(f"{index}.{task['task']} [{task['completed']}]")


def complete_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']}")

    try:
        choice = int(input("Enter task number to mark as completed: "))
    except ValueError:
        print("Invalid choice")
        return

    if choice>0 and choice<=len(tasks):
        choice = choice-1

        tasks[choice]["completed"] = "Y"

        print("Task marked as completed")
    else:
        print("Number out of range")


def delete_task(tasks):
    if not tasks:
        print("No tasks available")
        return
    
    for index, task in enumerate(tasks,start=1):
        print(f"{index}.{task['task']} [{task['completed']}]")

    try:
        choice = int(input("Enter task number to delete: "))
    except ValueError:
        print("Invalid choice")
        return

    if choice>0 and choice <= len(tasks):
        choice = choice-1
        tasks.pop(choice)
        print("Task deleted successfully")
    else:
        print("Number out of range")

def tasks_menu():
    while True:
        try:
            choice = int(input("Tasks Menu\n1-Add tasks\n2-View tasks\n3-Complete tasks\n4-Back\n"))
        except ValueError:
            print("Invalid input")
            continue

        match choice:
            case 1:
                add_task(tasks)
            case 2:
                view_tasks(tasks)
            case 3:
                complete_tasks(tasks)
            case 4:
                break
            case _:
                print("Wrong choice")


if __name__=="__main__":

    tasks_menu()
