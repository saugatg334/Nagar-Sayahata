# Setup and Run Guide

## Prerequisites

- Python 3.8+
- MariaDB/MySQL
- Windows/Linux/Mac

## 1. Activate Virtual Environment

**Windows PowerShell:**
```powershell
myenv\Scripts\activate
```

**Windows CMD:**
```cmd
myenv\Scripts\activate.bat
```

**Git Bash / Linux / Mac:**
```bash
source myenv/bin/activate
```

After activation, command prompt shows `(myenv)` prefix.

## 2. Install Requirements

Run in project root (where `requirements.txt` is located):
```bash
pip install -r requirements.txt
```

## 3. Database Setup

### Create Database

Open MySQL client (phpMyAdmin, MySQL Workbench, or command line):
```sql
CREATE DATABASE nagar_sahayata_db;
```

### Verify Settings

Database settings in `myproject/config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nagar_sahayata_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 4. Run Migrations

All Django commands must run from `myproject/` folder (where `manage.py` is located):

```bash
cd myproject
python manage.py makemigrations
python manage.py migrate
```

## 5. Run Server

```bash
python manage.py runserver
```

## 6. Access Application

| URL | Description |
|-----|-------------|
| http://127.0.0.1:8000/ | Home page (Frontend) |
| http://127.0.0.1:8000/frontend/navbar/ | Frontend navbar page |
| http://127.0.0.1:8000/admin/login/ | Admin login |

## 7. Static Files

Static files are served from two locations:
- Backend static: `myproject/backend/static/`
- Frontend static: `myproject/frontend/static/`

Both configured in `settings.py`:
```python
STATICFILES_DIRS = [
    BASE_DIR / "backend" / "static",
    BASE_DIR / "frontend" / "static",
]
```

## 8. Templates

Templates are loaded from:
- `myproject/backend/templates/`
- `myproject/frontend/templates/`

Configured in `settings.py`:
```python
TEMPLATES = [{
    'DIRS': [
        BASE_DIR / "backend" / "templates",
        BASE_DIR / "frontend" / "templates",
    ],
}]
```

## Quick Checklist

- [ ] Virtual environment (myenv) activated
- [ ] Requirements installed
- [ ] Database created in MySQL
- [ ] Migrations run (makemigrations + migrate)
- [ ] Server running from myproject/ folder