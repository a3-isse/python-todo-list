from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="PASSWORD",
        database="todo_app"
    )


@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)