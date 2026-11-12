import math
import random
from datetime import date, timedelta
SESSION_LENGTHS = (25, 45, 60)
def show_menu():
    print("\nStudy Planner\n")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Show summary")
    print("5. Suggest a task")
    print("6. Exit")
def ask_text(prompt):
    """Keep asking until the user types something that is not empty."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty. Please try again.")
def ask_int(prompt, minimum=None, maximum=None):
    """Keep asking until the user types a whole number inside the given range."""
    while True:
        text = input(prompt).strip()
        try:
            number = int(text)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if minimum is not None and number < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.")
            continue
        if maximum is not None and number > maximum:
            print(f"Please enter a number less than or equal to {maximum}.")
            continue
        return number
def add_task(tasks):
    course = ask_text("Course: ")
    description = ask_text("Task: ")
    minutes = ask_int("Estimated minutes: ", minimum=1)
    days = ask_int("Due in days: ", minimum=0)

    due_date = date.today() + timedelta(days=days)
    task = {
        "course": course,
        "description": description,
        "minutes": minutes,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    print(f"Task added: {course} - {description}")
def view_tasks(tasks):
    if not tasks:
        print("No tasks yet")
        return
    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['course']} - {task['description']}")
        print(f"   Estimated minutes: {task['minutes']}")
        print(f"   Due date: {task['due_date'].strftime('%d/%m/%Y')}")
        print(f"   Status: {status}")
def complete_task(tasks):
    if not tasks:
        print("No tasks yet")
        return
    number = ask_int(f"Task number (1-{len(tasks)}): ", minimum=1, maximum=len(tasks))
    task = tasks[number - 1]
    if task["completed"]:
        print(f"Task {number} is already completed.")
    else:
        task["completed"] = True
        print(f"Task {number} marked as completed.")
def show_summary(tasks):
    if not tasks:
        print("No tasks yet, so there is no summary to show.")
        return
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    remaining = total - completed
    progress = completed / total * 100
    remaining_minutes = sum(task["minutes"] for task in tasks if not task["completed"])
    courses = {task["course"] for task in tasks}

    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Remaining: {remaining}")
    print(f"Progress: {progress:.0f}%")
    print(f"Estimated minutes left: {remaining_minutes}")
    print("Courses: " + ", ".join(sorted(courses)))
def suggest_task(tasks):
    pending = []
    for task in tasks:
        if not task["completed"]:
            pending.append(task)
    if not pending:
        print("No pending tasks to suggest. Great job!")
        return
    task = random.choice(pending)
    print(f"Suggested task: {task['course']} - {task['description']}")
    print(f"Estimated minutes: {task['minutes']}")
    print("Choose a session length:")
    for number, length in enumerate(SESSION_LENGTHS, start=1):
        print(f"{number}. {length} minutes")
    choice = ask_int(f"Your choice (1-{len(SESSION_LENGTHS)}): ", minimum=1, maximum=len(SESSION_LENGTHS))
    session_length = SESSION_LENGTHS[choice - 1]
    sessions_needed = math.ceil(task["minutes"] / session_length)
    print(f"You need {sessions_needed} session(s) of {session_length} minutes.")
def main():
    tasks = []
    try:
        while True:
            show_menu()
            choice = ask_int("Choose an option (1-6): ", minimum=1, maximum=6)
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                complete_task(tasks)
            elif choice == 4:
                show_summary(tasks)
            elif choice == 5:
                suggest_task(tasks)
            elif choice == 6:
                print("Exiting Study Planner. Good luck with your studies!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nExiting Study Planner. Good luck with your studies!")
if __name__ == "__main__":
    main()
