import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo, clear_completed_todos

console = Console()
app = typer.Typer()


@app.command(short_help='Add a task')
def add(task: str, category: str, priority: str = 'Medium', deadline: str = None):
    """Add a task with optional priority and deadline."""
    typer.echo(f"Adding {task} - Category: {category}, Priority: {priority}, Deadline: {deadline}")
    todo = Todo(task, category, priority, deadline)
    insert_todo(todo)
    show()


@app.command()
def delete(position: int):
    """Delete a task by position."""
    typer.echo(f"Deleting task {position}")
    delete_todo(position - 1)
    show()


@app.command()
def complete(position: int):
    """Mark a task as complete."""
    typer.echo(f"Completing task {position}")
    complete_todo(position - 1)
    show()


@app.command()
def update(position: int, task: str = None, category: str = None, priority: str = None, deadline: str = None):
    """Update task details."""
    typer.echo(f"Updating task {position}")
    update_todo(position - 1, task, category, priority, deadline)
    show()


@app.command()
def clear_completed():
    """Clear all completed tasks."""
    typer.echo("Clearing completed tasks")
    clear_completed_todos()
    show()


@app.command()
def show():
    """Display all tasks."""
    tasks = get_all_todos()
    console.print("[bold magenta]Todo List[/bold magenta]", "✅")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Task", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Priority", min_width=10, justify="center")
    table.add_column("Deadline", min_width=12, justify="center")
    table.add_column("Status", min_width=12, justify="center")

    for idx, task in enumerate(tasks, start=1):
        status_str = "✅" if task.status == 2 else "🔄" if task.status == 1 else "❌"
        deadline_str = task.deadline if task.deadline else "-"
        table.add_row(str(idx), task.task, task.category, task.priority, deadline_str, status_str)
    console.print(table)


if __name__ == "__main__":
    app()
