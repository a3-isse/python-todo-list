# Flask To-Do List App

A simple To-Do web application built using:

- Python
- Flask
- MySQL
- OOP (Class Inheritance)
- Exception Handling
- Unit Testing

---

## Features

- Add new tasks
- Mark tasks as complete
- Delete tasks
- View all tasks ordered by newest first
- Database error handling
- Object-oriented structure
- Basic unit test included

---

## Project Structure

```
project/
│
├── main.py
├── models.py
├── templates/
│   └── index.html
├── README.md
└── tests/
    └── test_tasks.py
```

---

## Database Setup

1. Create database:

```sql
CREATE DATABASE todo_app;
USE todo_app;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## How To Run

1. Activate virtual environment:

```bash
source .venv/Scripts/activate
```

2. Run application:

```bash
python main.py
```

3. Open browser:

```
http://127.0.0.1:5000
```

---

## OOP Design

The application uses:

- `Database` base class
- `Task` class that inherits from `Database`
- CRUD methods implemented inside `Task`

---

## Exception Handling

All database operations are wrapped in try/except blocks to prevent application crashes and provide error logging.

---

## Unit Testing

A basic unit test is included to test task creation functionality.

Run tests with:

```bash
python -m unittest test_task.py
```

---

## Author

Ahmed Isse