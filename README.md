# 🎓 Student Organizer App (Python + MS SQL)

This is a *Student Organizer App* built using *Python* and *MS SQL Server*.  
It allows students to:
- ✅ Manage their *To-Do tasks*
- 📝 Organize *Notes* (subject, topic, subtopic, content)
- 📅 Keep track of *Deadlines*  

All the data is stored in a *SQL Server database* for persistence.  

---

## 📂 Project Structure
StudentOrganizer/
│── main.py              # Main menu / homepage
│── todo_app.py          # ToDoApp functions
│── notes_app.py         # Notes functions
│── deadlines_app.py     # Deadlines functions
│── dashboard.py         # Student Dashboard overview
│── db_config.py         # Database connection file
│── README.md            # Documentation

---

## 🛠 Database Setup

1. Install *SQL Server* and *SQL Server Management Studio (SSMS)*.
2. Open SSMS and create a new database called:

```sql
CREATE DATABASE CollegeOrganizer;

-- Table for To-Do Tasks
CREATE TABLE ToDoApp (
    id INT IDENTITY(1,1) PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL
);

-- Table for Notes
CREATE TABLE NotesHeader (
    id INT IDENTITY(1,1) PRIMARY KEY,
    subject VARCHAR(100) NOT NULL,
    topic VARCHAR(100) NOT NULL,
    subtopic VARCHAR(100),
    content TEXT
);

-- Table for Deadlines
CREATE TABLE Deadlines (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    deadline_date VARCHAR(50) NOT NULL
);



Make database connection:
import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=YOUR_SERVER_NAME;"   # Change this to your SQL Server name
        "Database=CollegeOrganizer;"
        "Trusted_Connection=yes;"
    )
    return conn
