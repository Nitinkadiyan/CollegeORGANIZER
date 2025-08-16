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
