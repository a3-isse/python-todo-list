from flask import Flask, request, redirect, render_template
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("MYSQL_PASSWORD")

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= password,
        database="todo_app"
    )

class Database:
    def __init__(self):
        try:
            self.conn = get_db_connection()
            self.cursor = self.conn.cursor(dictionary=True)
        except Error as e:
            print(f"Database connection error: {e}")
            self.conn = None
            self.cursor = None

    def commit(self):
        if self.conn:
            try:
                self.conn.commit()
            except Error as e:
                print(f"Commit error: {e}")

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Error as e:
            print(f"Close connection error: {e}")
        
class Task(Database):

    def get_all(self):
        if not self.cursor:
            return []

        try:
            self.cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error fetching tasks: {e}")
            return []

    def create(self, title):
        if not self.cursor:
            return

        try:
            self.cursor.execute(
                "INSERT INTO tasks (title) VALUES (%s)",
                (title,)
            )
            self.commit()
        except Error as e:
            print(f"Error creating task: {e}")

    def mark_complete(self, task_id):
        if not self.cursor:
            return

        try:
            self.cursor.execute(
                "UPDATE tasks SET completed = TRUE WHERE id = %s",
                (task_id,)
            )
            self.commit()
        except Error as e:
            print(f"Error updating task: {e}")

    def delete_task(self, task_id):
        if not self.cursor:
            return

        try:
            self.cursor.execute(
                "DELETE FROM tasks WHERE id = %s",
                (task_id,)
            )
            self.commit()
        except Error as e:
            print(f"Error deleting task: {e}")

@app.route("/")
def index():
    task_model = Task()
    tasks = task_model.get_all()
    task_model.close()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    task_model = Task()
    task_model.create(title)
    task_model.close()
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete(task_id):
    task_model = Task()
    task_model.mark_complete(task_id)
    task_model.close()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    task_model = Task()
    task_model.delete_task(task_id)
    task_model.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)