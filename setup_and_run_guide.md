# Setup and Run Guide - Smart Municipal Grievance System

## 1. Virtual Environment Setup (myenv)

### Create virtual environment
```
python -m venv myenv
```

### Activate virtual environment

**Windows PowerShell:**
```
myenv\Scripts\activate
```

**Windows CMD:**
```
myenv\Scripts\activate.bat
```

**Git Bash / Linux / Mac:**
```
source myenv/bin/activate
```

After activation, you will see `(myenv)` at the start of your command line. This means the virtual environment is active and ALL commands below must be run in this state.

---

## 2. Install Requirements

Run this command in the project root (where requirements.txt is located):
```
pip install -r requirements.txt
```

---

## 3. Project Run Location Rule

Django commands MUST be run inside the `myproject/` folder (where manage.py is located).

Example:
```
cd myproject
```

---

## 4. Database Setup (MariaDB/MySQL)

### Configure in settings.py
Open `myproject/config/settings.py` and locate the `DATABASES` section. Change these fields:
- **NAME**: Your database name
- **USER**: Your MySQL username
- **PASSWORD**: Your MySQL password
- **HOST**: localhost (or your server IP)
- **PORT**: 3306 (default MySQL port)

### Create database in MySQL
Open your MySQL client (phpMyAdmin, MySQL Workbench, or command line) and run:
```
CREATE DATABASE your_database_name;
```

### Run migrations
After DB setup, inside `myproject/` folder run:
```
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Run Project

1. Activate virtual environment (myenv)
2. Go to myproject folder: `cd myproject`
3. Run server:
```
python manage.py runserver
```

---

## 6. Browser Link

- **Main URL**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Login Page**: http://127.0.0.1:8000/login/

---

## 7. Required Packages

- Django
- mysqlclient
- Pillow
- python-dotenv

---

## 8. Final Checklist

- [ ] Virtual environment (myenv) is activated
- [ ] requirements.txt is installed
- [ ] Database is created in MySQL
- [ ] Migrations are done (makemigrations + migrate)
- [ ] Server is running from myproject/ folder
