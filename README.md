# Study Planner

A small text-based Python program that helps a student organize study tasks.

## Features

- Add a study task with a course name, description, estimated minutes, and due date (counted from today).
- View all tasks with their number, course, estimated minutes, due date, and status (`Pending` or `Completed`).
- Mark a task as completed. The program checks for invalid numbers and tasks that are already completed.
- Show a summary: total tasks, completed, remaining, progress percentage, estimated minutes left, and the list of courses.
- Suggest a random pending task and calculate how many study sessions (25, 45, or 60 minutes) it needs.
- Input validation: invalid input shows a message and asks again without crashing.

## Requirements

- Python 3.8 or newer
- No external packages. It uses only the standard library (`math`, `random`, `datetime`).

## How to Run

### Option 1: Run from the terminal

```bash
python study_planner.py
```

### Option 2: Run in Google Colab

1. Open [Study Planner.ipynb](Study%20Planner.ipynb) in Google Colab (File → Upload notebook).
2. Run the code cell. The menu appears and waits for your input.

## Menu

```
Study Planner

1. Add a task
2. View tasks
3. Complete a task
4. Show summary
5. Suggest a task
6. Exit
```

Type a number from 1 to 6 and press Enter. After each action, the menu appears again. Choose `6` to exit.

## Notes

- Tasks are stored in memory only. They are lost when the program stops.
- All messages, variable names, and function names are in English.

## Project Files

- `study_planner.py`: the full program.
- `Study Planner.ipynb`: the Colab notebook with an explanation, the code, and notes on the interface fix.
- `README.md`: this file.

## Main Functions

- `add_task(tasks)`
- `view_tasks(tasks)`
- `complete_task(tasks)`
- `show_summary(tasks)`
- `suggest_task(tasks)`
