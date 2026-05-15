# Project Structure

## Root Directory Layout

```
6-sem project/
│
├── myenv/                          # Virtual environment
├── myproject/                     # Django project root
├── frontend/                      # Inactive duplicate frontend (NOT USED)
├── docs/                          # Documentation markdown files
│   ├── project_structure.md
│   ├── project_goal.md
│   ├── current_flow.md
│   └── setup_and_run_guide.md
├── README.md
├── requirements.txt
└── git-commands.md
```

## Django Project Structure (myproject/)

```
myproject/
│
├── config/                        # Django settings and configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── backend/                       # Backend applications
│   ├── apps/
│   │   ├── admin_panel/           # Admin panel app
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── migrations/
│   │   └── admin_auth/            # Admin authentication app
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── models.py
│   │       ├── urls.py
│   │       ├── views.py
│   │       └── migrations/
│   │
│   ├── static/                    # Backend static files
│   │   ├── css/
│   │   │   ├── admin_panel/
│   │   │   ├── authentication/
│   │   │   ├── home/
│   │   │   └── profile/
│   │   ├── js/
│   │   │   └── admin_panel/
│   │   └── fonts/
│   │
│   └── templates/                 # Backend templates
│       ├── admin_base.html
│       ├── admin_panel.html
│       ├── authentication/
│       │   └── login.html
│       ├── home/
│       │   └── home.html
│       └── profile/
│           └── index.html
│
├── frontend/                      # ACTIVE frontend application
│   ├── apps/
│   │   ├── core/                  # Core frontend app (ACTIVE)
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── migrations/
│   │   └── user_auth/            # User authentication app
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── models.py
│   │       ├── urls.py
│   │       ├── views.py
│   │       └── migrations/
│   │
│   ├── static/                   # Frontend static files (ACTIVE)
│   │   └── css/
│   │       └── core/
│   │           └── style.css
│   │
│   └── templates/                # Frontend templates (ACTIVE)
│       ├── core/
│       │   └── index.html        # Main home page (ACTIVE)
│       ├── home/
│       │   └── index.html
│       └── user_auth/
│           └── index.html
│
├── db.sqlite3
└── manage.py
```

## Key Directories

### Active Frontend
- Location: `myproject/frontend/`
- Template: `myproject/frontend/templates/core/index.html`
- CSS: `myproject/frontend/static/css/core/style.css`

### Static Files Configuration
- Backend static: `myproject/backend/static/`
- Frontend static: `myproject/frontend/static/`
- Both configured in `settings.py` via `STATICFILES_DIRS`

### Template Configuration
- Backend templates: `myproject/backend/templates/`
- Frontend templates: `myproject/frontend/templates/`
- Both configured in `settings.py` via `DIRS` in TEMPLATES

### Inactive Duplicate
- Root-level `frontend/` folder exists but is not active
- Active frontend is in `myproject/frontend/`

## Installed Apps

```python
# Backend apps
'backend.apps.admin_panel'
'backend.apps.admin_auth'

# Frontend apps
'frontend.apps.core'
'frontend.apps.user_auth'
```