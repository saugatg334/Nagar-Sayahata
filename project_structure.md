# FINAL CLEAN PROFESSIONAL DJANGO STRUCTURE

## Project Structure

```
6-sem project/
│
├── all_details.txt
├── project_overview.md
├── project_structure.md
├── README.md
├── requirements.txt
│
├── myenv/                          # Virtual environment (NOT part of Django runtime)
│   ├── pyvenv.cfg
│   ├── Include/
│   ├── Lib/
│   │   └── site-packages/
│   │       ├── asgiref/
│   │       ├── django/
│   │       ├── dotenv/
│   │       ├── mysqlclient-2.2.8.dist-info/
│   │       ├── MySQLdb/
│   │       ├── PIL/
│   │       ├── pillow-12.2.0.dist-info/
│   │       ├── pip/
│   │       ├── pip-26.1.1.dist-info/
│   │       ├── python_dotenv-1.2.2.dist-info/
│   │       ├── sqlparse/
│   │       ├── sqlparse-0.5.5.dist-info/
│   │       ├── tzdata/
│   │       └── tzdata-2026.2.dist-info/
│   └── Scripts/
│       ├── activate
│       ├── activate.bat
│       ├── Activate.ps1
│       └── deactivate.bat
│
└── myproject/                      # Django project root
    │
    ├── config/                     # Django settings and configuration
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py             # Main settings
    │   ├── urls.py                 # Main URL configuration
    │   └── wsgi.py
    │
    ├── backend/                    # Backend application code
    │   ├── apps/                   # Django apps
    │   │   ├── admin_panel/        # Admin panel app
    │   │   │   ├── __init__.py
    │   │   │   ├── admin.py
    │   │   │   ├── apps.py
    │   │   │   ├── models.py
    │   │   │   ├── tests.py
    │   │   │   ├── urls.py
    │   │   │   ├── views.py
    │   │   │   └── migrations/
    │   │   │       └── __pycache__/
    │   │   └── authentication/     # Authentication app
    │   │       ├── __init__.py
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── models.py
    │   │       ├── tests.py
    │   │       ├── urls.py
    │   │       ├── views.py
    │   │       └── migrations/
    │   │           ├── 0001_initial.py
    │   │           ├── 0002_skill.py
    │   │           ├── 0003_contactinfo_message_sociallink.py
    │   │           ├── 0004_delete_contactinfo_delete_message_delete_sociallink.py
    │   │           ├── 0005_contactinfo_message_sociallink.py
    │   │           ├── 0006_delete_about_delete_aboutstat_delete_contactinfo_and_more.py
    │   │           ├── __init__.py
    │   │           └── __pycache__/
    │   │
    │   ├── media/                  # User-uploaded files
    │   ├── static/                 # Static files (CSS, JS, images)
    │   │   ├── css/
    │   │   │   ├── admin_panel/
    │   │   │   │   └── style.css
    │   │   │   ├── authentication/
    │   │   │   │   └── login.css
    │   │   │   └── home/
    │   │   │       └── home.css
    │   │   ├── fonts/
    │   │   │   └── remixicon.woff2
    │   │   └── js/
    │   │       ├── admin_panel/
    │   │       │   ├── app.js
    │   │       │   ├── bootstrap.bundle.min.js
    │   │       │   ├── dataTables.min.js
    │   │       │   ├── iconify-icon.min.js
    │   │       │   ├── jquery-3.7.1.min.js
    │   │       │   ├── jquery-jvectormap-world-mill-en.js
    │   │       │   └── script.js
    │   │       └── authentication/
    │   │
    │   └── templates/              # Django templates
    │       ├── admin_base.html
    │       ├── admin_panel.html
    │       ├── authentication/
    │       │   └── login.html
    │       └── home/
    │           └── home.html
    │
    ├── staff_portal/               # Empty placeholder folder
    ├── db.sqlite3
    └── manage.py
```

## Environment Info

### Virtual Environment (myenv)
- `myenv/` is the Python virtual environment created using `python -m venv myenv`.
- It contains isolated Python packages and scripts required for the project.
- This folder is NOT part of the Django project runtime and should not be committed to version control (typically added to `.gitignore`).
- Activation scripts are located in `myenv/Scripts/` (Windows) or `myenv/bin/` (Unix-like systems).
- All project dependencies (Django, Pillow, etc.) are installed within this environment to avoid conflicts with system Python.

### Relation to Project
- The virtual environment ensures that the project's Python dependencies are managed separately from the global Python installation.
- Commands like `pip install` and `python manage.py` should be run with the virtual environment activated.

## Main Project Root

### Django Project Root (myproject/)
- `myproject/` is the main Django project directory containing all application code and configuration.
- `manage.py` is located here and is the entry point for Django management commands (e.g., `python manage.py runserver`).
- `config/` folder contains Django project settings (`settings.py`), URL configuration (`urls.py`), and WSGI/ASGI configurations.
- `backend/` folder houses reusable Django apps, static files, templates, and media uploads.

## Explanation of Structure

### Root application layout
- `config/` contains Django project settings and URL configuration.
- `backend/` contains reusable app modules, static assets, and templates.
- `staff_portal/` exists in the repository as an empty placeholder folder.
- `manage.py` is the Django management script.
- `db.sqlite3` is the local development database file.

### Backend apps
- `backend/apps/admin_panel/` is the admin dashboard app.
- `backend/apps/authentication/` handles login, logout, and user authentication.
- Each Django app includes `models.py`, `views.py`, `urls.py`, `admin.py`, `apps.py`, `tests.py`, and migrations.

### Templates
- Global templates are stored in `backend/templates/`.
- `admin_base.html` is the base layout used by admin pages.
- `admin_panel.html` is the admin dashboard page.
- `backend/templates/authentication/login.html` is the login page.
- `backend/templates/home/home.html` is the home page.

### Static files
- Static files are stored in `backend/static/`.
- CSS lives under `backend/static/css/` by section.
- JS lives under `backend/static/js/` by section.
- Font files live under `backend/static/fonts/`.
- `backend/static/css/admin_panel/style.css` and `backend/static/js/admin_panel/` contain admin-specific assets.
- `backend/static/css/authentication/login.css` contains login-specific styling.

### Media files
- `backend/media/` is reserved for uploaded media files in development.
- Media is served from `backend/media/` when configured in `settings.py`.

## Notes
- The folder name `admin_panel` is consistent across app names, templates, and static assets.
- Any old `admin_pannel` path names have been removed from the current workspace layout.
- The virtual environment `myenv/` is included for completeness but is not part of the Django application structure.

### Static files
- Static files are stored in `backend/static/`.
- CSS lives under `backend/static/css/` by section.
- JS lives under `backend/static/js/` by section.
- Font files live under `backend/static/fonts/`.
- `backend/static/css/admin_panel/style.css` and `backend/static/js/admin_panel/` contain admin-specific assets.
- `backend/static/css/authentication/login.css` contains login-specific styling.

### Media files
- `backend/media/` is reserved for uploaded media files in development.
- Media is served from `backend/media/` when configured in `settings.py`.

## Notes
- The folder name `admin_panel` is now consistent across app names, templates, and static assets.
- any old `admin_pannel` path names have been removed from the current workspace layout.
- If you want the documentation to include the full workspace root, add `README.md`, `requirements.txt`, and `myenv/` above `myproject/`.

