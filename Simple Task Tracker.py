tasks = []


def add_task(title: str) -> None:
    tasks.append({"title": title, "done": False})
    print(f'Added: "{title}"')


def complete_task(index: int) -> None:
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f'Completed: "{tasks[index]["title"]}"')
    else:
        print("Task number not found.")


def show_tasks() -> None:
    if not tasks:
        print("No tasks yet.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i + 1}. {status} {task['title']}")
    print()


# Example usage
add_task("Buy groceries")
add_task("Finish coding exercise")
complete_task(1)
show_tasks()
