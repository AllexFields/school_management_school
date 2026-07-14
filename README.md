# 🎓 School Management System (Python + MySQL)

A menu-driven School Management System developed using **Core Python**, **Object-Oriented Programming (OOP)** and **MySQL**.

This project demonstrates how a simple runtime-based Python application can be refactored into a modular application with persistent database storage using CRUD operations.

---

# 📖 Project Evolution

This repository contains two versions of the same project.

## 🔹 Version 1

The initial implementation was built using Python classes and objects.

Student records were stored inside a Python list, therefore all data was available only during program execution.

This version focuses on learning:

- Object-Oriented Programming
- Classes & Objects
- Loops
- Conditional Statements
- Functions
- Regular Expressions
- Menu Driven Programs

---

## 🔹 Version 2

The second version is a complete refactored implementation.

Instead of storing records inside a Python list, the application is connected to a MySQL database where student records are stored permanently.

This version introduces:

- MySQL Database Connectivity
- CRUD Operations
- Modular Project Structure
- Separation of Concerns
- Better Code Organization

---

# 📊 Version Comparison

| Feature | Version 1 | Version 2 |
|----------|:---------:|:---------:|
| Object-Oriented Programming (OOP) | ✅ | ✅ |
| Menu-Driven Interface | ✅ | ✅ |
| Runtime Data Storage (Python List) | ✅ | ❌ |
| MySQL Database Connectivity | ❌ | ✅ |
| CRUD Operations | ❌ | ✅ |
| Persistent Data Storage | ❌ | ✅ |
| Auto-Increment Student ID | ❌ | ✅ |
| Modular Project Structure | ❌ | ✅ |
| Separation of Concerns | ❌ | ✅ |
| Input Validation | ✅ | ✅ |
| Regular Expression (Regex) Validation | ✅ | ✅ |

---

# ✨ Features

- Add New Student
- View All Students
- Search Student by ID
- Update Student Standard
- Update Guardian Contact Number
- Delete Student Record
- Input Validation
- Regular Expression Validation
- Persistent Data Storage using MySQL

---

# 🛠 Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- Object-Oriented Programming (OOP)
- Regular Expressions (Regex)

---

# 📁 Project Structure

```text
School_Management_System/
│
├── Version_1/
│   └── school_management_v1.py
│
├── Version_2/
│   ├── database.py
│   ├── models.py
│   ├── operations.py
│   └── main.py
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🗄 Database Schema

Table Name : students

| Column | Data Type |
|---------|-----------|
| std_id | INT (AUTO_INCREMENT) |
| std_name | VARCHAR(100) |
| age | INT |
| standard | INT |
| guard_c_no | VARCHAR(10) |

---

# 🚀 How to Run

### 1 Clone the Repository

```bash
git clone <repository-url>
```

### 2 Install Dependencies

```bash
pip install -r requirements.txt
```

### 3 Create Database

```sql
CREATE DATABASE school_db;

USE school_db;

CREATE TABLE students(
    std_id INT PRIMARY KEY AUTO_INCREMENT,
    std_name VARCHAR(100),
    age INT,
    standard INT,
    guard_c_no VARCHAR(10)
);
```

### 4 Update Database Credentials

Open

Version_2/database.py

and update

- Host
- Username
- Password

---

### 5 Run the Application

```bash
cd Version_2

python main.py
```

---

# 📸 Screenshots

## Version 1

![Version1](Screenshots/01_original_runtime_program.png)

---

## Main Menu

![Menu](Screenshots/02_main_menu.png)

---

## Add Student

![Add Student](Screenshots/03_add_student.png)

---

## View Students

![View Students](Screenshots/04_view_students.png)

---

## Update Student

![Update Student](Screenshots/05_update_student.png)

---

## MySQL Database

![Database](Screenshots/07_mysql_database.png)

---

## Delete Record

![Structure](Screenshots/06_delete_student.png)

---

# 📚 What I Learned

Through this project I learned:

- Object-Oriented Programming
- Python Modules
- MySQL Connectivity
- CRUD Operations
- Regular Expressions
- Exception Handling
- Project Refactoring
- Modular Programming

---

# 🚀 Future Improvements

- Login Authentication
- GUI using Tkinter
- Export Student Data to Excel
- Search by Name
- Attendance Management
- Marks Management

---

# 👨‍💻 Author

Shivam Thakur

GitHub:
