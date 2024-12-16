# todo

This is a simple CLI-based To-Do application built using Python, utilizing the `typer` library for command-line interface handling and `rich` for enhanced console output.

## Features
- **Add Tasks:** Add new tasks with a category.
- **Delete Tasks:** Remove tasks by their position.
- **Update Tasks:** Update the task name or category.
- **Mark Complete:** Mark tasks as completed.
- **View Tasks:** Display all tasks in a tabular format.

---

## Requirements
- Python 3.7 or above
- `typer` library
- `rich` library

Install the required libraries using pip:
```bash
pip install typer rich
```

---

## Setup and Usage
1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Ensure you have a `model.py` and `database.py` file in the same directory, implementing the `Todo` class and required database methods (`get_all_todos`, `insert_todo`, `delete_todo`, `complete_todo`, `update_todo`).

3. Run the CLI application:
   ```bash
   python cli.py <command> [options]
   ```

---

## Commands
### Add a Task
```bash
python cli.py add "Task Name" "Category"
```

### Delete a Task
```bash
python cli.py delete <position>
```

### Update a Task
```bash
python cli.py update <position> --task "New Task Name" --category "New Category"
```

### Mark a Task as Complete
```bash
python cli.py complete <position>
```

### Show All Tasks
```bash
python cli.py show
```

---

## Example Usage
```bash
# Add tasks
python cli.py add "Finish Assignment" "Study"
python cli.py add "Play Football" "Sports"

# View tasks
python cli.py show

# Mark a task as complete
python cli.py complete 1

# Delete a task
python cli.py delete 2
```

---

Enjoy managing your tasks effortlessly with this CLI tool! 😊