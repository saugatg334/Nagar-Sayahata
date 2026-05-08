# Project Structure

This file documents only the current real workspace structure and current Django routing configuration.

## Current Workspace Tree

```
6-sem project/
├── .gitignore
├── README.md
├── all_details.txt
├── project_structure.md
├── requirements.txt
├── file_structure.md
├── myenv/
│   ├── pyvenv.cfg
│   ├── Include/
│   ├── Lib/
│   └── Scripts/
└── myproject/
    ├── manage.py
    ├── db.sqlite3
    ├── file_structure.md
    ├── config/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── backend/
        ├── apps/
        │   ├── admin_pannel/
        │   │   ├── __init__.py
        │   │   ├── admin.py
        │   │   ├── apps.py
        │   │   ├── models.py
        │   │   ├── tests.py
        │   │   ├── urls.py
        │   │   ├── views.py
        │   │   └── migrations/
        │   └── authentication/
        │       ├── __init__.py
        │       ├── admin.py
        │       ├── apps.py
        │       ├── models.py
        │       ├── tests.py
        │       ├── urls.py
        │       ├── views.py
        │       └── migrations/
        ├── templates/
        │   ├── admin_base.html
        │   ├── admin_pannel.html
        │   ├── authentication/
        │   │   └── login.html
        │   └── home/
        │       └── home.html
        ├── static/
        │   ├── admin_pannel/
        │   │   └── profile.png
        │   ├── css/
        │   │   ├── admin_pannel/
        │   │   ├── authentication/
        │   │   └── home/
        │   ├── fonts/
        │   └── js/
        │       ├── admin_pannel/
        │       └── authentication/
        └── media/
```

## Current Django Routing

### Root URL configuration
- `myproject/config/urls.py`
- Includes:
  - `path('', include('backend.apps.authentication.urls'))`
  - `path('admin/', include('backend.apps.admin_pannel.urls'))`

### Authentication app
- `myproject/backend/apps/authentication/urls.py`
- `app_name = 'auth'`
- Routes:
  - `path('login/', LoginView.as_view(), name='login')`
  - `path('logout/', LogoutView.as_view(), name='logout')`
- Active URLs:
  - `/login/`
  - `/logout/`

### Admin panel app
- `myproject/backend/apps/admin_pannel/urls.py`
- `app_name = 'admin_pannel'`
- Routes:
  - `path('', MainFunctionView.as_view(), name='main')`
  - `path('home/', Home.as_view(), name='home')`
- Active URLs:
  - `/admin/`
  - `/admin/home/`

## Current Template & Static Layout

- Templates are stored in `myproject/backend/templates/`.
- Static assets are stored in `myproject/backend/static/`.
- Media uploads are stored in `myproject/backend/media/`.

### Known template files
- `admin_base.html`
- `admin_pannel.html`
- `authentication/login.html`
- `home/home.html`

### Known static directories
- `myproject/backend/static/admin_pannel/`
- `myproject/backend/static/css/admin_pannel/`
- `myproject/backend/static/css/authentication/`
- `myproject/backend/static/css/home/`
- `myproject/backend/static/fonts/`
- `myproject/backend/static/js/admin_pannel/`
- `myproject/backend/static/js/authentication/`

## Current URL naming conventions

- Auth URLs must be referenced with `auth:login` and `auth:logout`.
- Admin panel URLs must be referenced with `admin_pannel:main` and `admin_pannel:home`.
- Example template usage:
  - `{% url 'auth:login' %}`
  - `{% url 'auth:logout' %}`
  - `{% url 'admin_pannel:home' %}`

## Current behavior notes

- The auth app is mounted at the project root.
- The admin panel app is mounted under `/admin/`.
- There is no built-in Django admin route configured in `config/urls.py`.
- `LogoutView` should redirect to `auth:login`.
- `LoginView` may redirect authenticated users to `admin_pannel:home`.

## How to run the current project

```powershell
cd "d:\ALL Coding\Collage project\6-sem project\myproject"
.\..\myenv\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver
```

Open `http://localhost:8000/` in the browser.