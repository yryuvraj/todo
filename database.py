import sqlite3
from typing import List
import datetime
from model import Todo

conn = sqlite3.connect('todos.db')
c = conn.cursor()


def create_table():
    c.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            task TEXT,
            category TEXT,
            priority TEXT,
            deadline TEXT,
            date_added TEXT,
            date_completed TEXT,
            status INTEGER,
            position INTEGER
        )""")

create_table()


def insert_todo(todo: Todo):
    c.execute('SELECT COUNT(*) FROM todos')
    count = c.fetchone()[0]
    todo.position = count if count else 0
    with conn:
        c.execute('''INSERT INTO todos VALUES (:task, :category, :priority, :deadline, :date_added, :date_completed, :status, :position)''',
                  {'task': todo.task, 'category': todo.category, 'priority': todo.priority, 'deadline': todo.deadline,
                   'date_added': todo.date_added, 'date_completed': todo.date_completed, 'status': todo.status, 'position': todo.position})


def get_all_todos() -> List[Todo]:
    c.execute('SELECT * FROM todos')
    results = c.fetchall()
    todos = [Todo(*result) for result in results]
    return todos


def delete_todo(position: int):
    c.execute('SELECT COUNT(*) FROM todos')
    count = c.fetchone()[0]
    with conn:
        c.execute("DELETE FROM todos WHERE position=:position", {"position": position})
        for pos in range(position + 1, count):
            change_position(pos, pos - 1, False)


def change_position(old_position: int, new_position: int, commit=True):
    c.execute('UPDATE todos SET position = :new_position WHERE position = :old_position',
              {'old_position': old_position, 'new_position': new_position})
    if commit:
        conn.commit()


def update_todo(position: int, task: str = None, category: str = None, priority: str = None, deadline: str = None):
    with conn:
        if task:
            c.execute('UPDATE todos SET task = :task WHERE position = :position', {'task': task, 'position': position})
        if category:
            c.execute('UPDATE todos SET category = :category WHERE position = :position', {'category': category, 'position': position})
        if priority:
            c.execute('UPDATE todos SET priority = :priority WHERE position = :position', {'priority': priority, 'position': position})
        if deadline:
            c.execute('UPDATE todos SET deadline = :deadline WHERE position = :position', {'deadline': deadline, 'position': position})


def complete_todo(position: int):
    with conn:
        c.execute('UPDATE todos SET status = 2, date_completed = :date_completed WHERE position = :position',
                  {'position': position, 'date_completed': datetime.datetime.now().isoformat()})


def clear_completed_todos():
    with conn:
        c.execute('DELETE FROM todos WHERE status = 2')
