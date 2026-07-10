# 🎓 Student Grade Management System

A simple **Python-based Student Grade Management System** that allows users to manage student records using a **JSON file** for data storage. This project demonstrates file handling, JSON operations, CRUD functionality, and basic grade calculation.

## 📌 Features

* ➕ Add new student records
* ✏️ Update existing student records
* ❌ Delete student records
* 🔍 Search student records by Student ID
* 📊 Calculate percentage
* 🏆 Calculate grade based on percentage
* 💾 Store records permanently using a JSON file
* 🖥️ Easy-to-use command-line interface (CLI)

---

## 📂 Project Structure

```text
StudentGrade-Management-System/
│
├── main.py
├── student_records.json
└── README.md
```

> **Note:** The `student_records.json` file will be created automatically when the program is run for the first time if it does not already exist.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or later

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## ▶️ Running the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/StudentGrade-Management-System.git
```

2. Navigate to the project directory:

```bash
cd StudentGrade-Management-System
```

3. Run the program:

```bash
python main.py
```

---

## 📋 Menu Options

When the program starts, you'll see the following menu:

```text
Student Grade Management System

1. Add Student Record
2. Update Student Record
3. Delete Student Record
4. Search Student Record
5. Calculate Percentage
6. Calculate Grade
```

Type:

```text
!exit
```

or

```text
!stop
```

to close the application.

---

## 💾 Student Record Format

Each student is stored using their **Student ID** as the unique key.

Example:

```json
{
    "101": {
        "name": "John",
        "age": 16,
        "class": "10",
        "physics_marks": 85,
        "chemistry_marks": 90,
        "mathematics_marks": 88
    }
}
```

---

## 📊 Percentage Calculation

The percentage is calculated using the formula:

```text
Percentage = (Physics + Chemistry + Mathematics) / 300 × 100
```

---

## 🏆 Grade Criteria

| Percentage | Grade |
| ---------- | ----- |
| 90 – 100   | A     |
| 80 – 89    | B     |
| 70 – 79    | C     |
| 60 – 69    | D     |
| Below 60   | F     |

---

## 🛠 Technologies Used

* Python 3
* JSON
* os Module

---

## 📚 Concepts Demonstrated

* Python Functions
* File Handling
* JSON Read/Write
* Dictionary Operations
* CRUD Operations
* Conditional Statements
* Loops
* Modular Programming
* Command-Line Interface (CLI)

---

## ⚠ Current Limitations

* No input validation for marks or age
* Duplicate Student IDs overwrite existing records
* No exception handling for invalid input
* Windows-specific file path
* Data stored locally only (no database)

---

## 🔮 Future Improvements

* Input validation
* Exception handling
* Cross-platform file paths using `pathlib`
* Student list display
* GPA calculation
* Subject-wise average
* Ranking system
* Database integration (SQLite/MySQL)
* Graphical User Interface (Tkinter or PyQt)
* Export records to CSV or Excel

---

## 🤝 Contributing

Contributions are welcome!

If you have suggestions or improvements:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it for educational purposes.

---

## 👨‍💻 Author

Developed as a Python practice project to demonstrate file handling, JSON data management, and CRUD operations.

⭐ If you found this project useful, consider giving it a star on GitHub!
