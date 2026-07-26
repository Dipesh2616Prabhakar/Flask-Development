# Employee Management System 🚀

A Flask + MySQL based Employee Management System with full CRUD functionality, extended with advanced features: **pagination, searching, sorting, and filtering**, plus a custom-designed, responsive UI.

Built on top of the original Flask-Development learning repository by Gagan Rajput.

---

## 📁 Project Structure

Flask-Development/
│
├── app/
│ ├── models/
│ ├── routes/
│ ├── templates/
│ ├── static/
│ ├── utils/
│ └── init.py
│
├── migrations/
├── app.py
├── config.py
├── requirements.txt
└── README.md


---

## 🛠 Prerequisites

- Python 3.11+
- MySQL Server (e.g. via XAMPP)
- Git

Check your Python version:
```bash
python --version
```

---

## 📥 Clone Repository

```bash
git clone https://github.com/<your-username>/Flask-Development.git
cd Flask-Development
```

---

## 🐍 Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗃 Database Setup

1. Start MySQL (e.g. via XAMPP Control Panel — start both Apache and MySQL).
2. Create a database named `employee_db` (via phpMyAdmin: `New` → name it `employee_db` → `Create`).
3. Update `config.py` with your MySQL credentials:
```python
   SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:<password>@localhost:3306/employee_db"
```
4. Run migrations to create the tables:
```bash
   set FLASK_APP=app.py        # Windows
   export FLASK_APP=app.py     # Linux/macOS

   flask db upgrade
```

---

## ▶️ Run the Application

```bash
python app.py
```

Then visit:

http://127.0.0.1:5000/home


---

## ✨ Features

### Core CRUD
- Add, view, update, and delete employee records.

### Advanced Data Management
- **Pagination** — 5 or 10 records per page, with page numbers and Previous/Next navigation, always showing current page and total record count.
- **Search** — search employees by Name, Email, or Department.
- **Sorting** — sort by Name, Email, Department, or Salary, ascending or descending, via clickable table headers.
- **Filtering** — filter by Department and by Salary range (min/max).
- **Combined functionality** — search, filter, sort, and pagination all work together simultaneously, and selected parameters persist across page navigation.

### UI/UX
- Custom-designed interface with a dark navbar, hero dashboard section, and badge-style stat cards.
- Department overview page showing employee count and average salary per department.
- Responsive Bootstrap-based layout across all pages.
- Clean search & filter panel, styled tables, and proper "no records found" messaging.

---

## 🗂 Routes Overview

| Route | Description |
|---|---|
| `/home` | Dashboard with employee/department stats |
| `/employee/list` | Employee roster with pagination, search, sort, filter |
| `/employee/add` | Add a new employee |
| `/employee/employeeDetail/<id>` | View employee details |
| `/employee/employeeUpdate/<id>` | Edit an employee |
| `/employee/employeeDelete/<id>` | Delete an employee |
| `/department` | Department overview |

---

## 👨‍💻 Author

Based on the original repository by **Gagan Rajput** (https://github.com/Gagan47raj), extended by **Dipesh Prabhakar**.

