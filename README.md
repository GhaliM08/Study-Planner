# Study Planner

A text-based Python program that helps a student organize study tasks: add tasks, track progress, and get suggestions on what to study next.

This is a course project. It uses only `print()` and `input()` and runs in the terminal.

## Features

- Add a study task with a course name, description, estimated minutes, and due date (counted from the day the program runs).
- View all tasks with their number, course, estimated minutes, due date, and status (`Pending` or `Completed`).
- Mark a task as completed. The program rejects invalid numbers and tasks that are already completed.
- Show a summary: total tasks, completed, remaining, progress percentage, estimated minutes left, and the list of courses (no repeats).
- Suggest a random pending task and calculate how many study sessions (25, 45, or 60 minutes) it needs.
- Input validation: invalid input shows a message and asks again without crashing.

## Requirements

- Python 3.8 or newer
- No external packages. It uses only the standard library (`math`, `random`, `datetime`).

## How to Run

Open a terminal in the project folder and run:

```bash
python study_planner.py
```

The menu appears and waits for your input:

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

## Notebook

[Study Planner.ipynb](Study%20Planner.ipynb) is a Jupyter notebook that explains the project and contains the full code in one cell. It can be opened in Jupyter, VS Code, or Google Colab. The notebook is a companion to the program, and `study_planner.py` is the version to run.

## Notes

- Tasks are stored in memory only, so they are lost when the program stops.
- All messages, variable names, and function names are in English.

## Project Files

- `study_planner.py`: the full program.
- `Study Planner.ipynb`: the project explanation and code, as a notebook.
- `README.md`: this file.

## Main Functions

- `add_task(tasks)`
- `view_tasks(tasks)`
- `complete_task(tasks)`
- `show_summary(tasks)`
- `suggest_task(tasks)`
