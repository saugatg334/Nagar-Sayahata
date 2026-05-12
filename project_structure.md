# FINAL CLEAN PROFESSIONAL DJANGO STRUCTURE

## Project Structure

```
myproject/
│
├── config/                          # Django settings and configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                  # Main settings
│   ├── urls.py                      # Main URL configuration
│   └── wsgi.py
│
├── backend/                         # Backend application code
│   ├── apps/                        # Django apps
│   │   ├── admin_panel/             # Admin panel app
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── migrations/
│   │   │       └── __pycache__/
│   │   └── authentication/          # Authentication app
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
│   ├── media/                       # User-uploaded files
│   ├── static/                      # Static files (CSS, JS, images)
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
│   
│   └── templates/                   # Django templates
│       ├── admin_base.html
│       ├── admin_panel.html
│       ├── authentication/
│       │   └── login.html
│       └── home/
│           └── home.html
│
├── staff_portal/                   # Empty placeholder folder
├── db.sqlite3
└── manage.py
```

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
- The folder name `admin_panel` is now consistent across app names, templates, and static assets.
- any old `admin_pannel` path names have been removed from the current workspace layout.
- If you want the documentation to include the full workspace root, add `README.md`, `requirements.txt`, and `myenv/` above `myproject/`.

