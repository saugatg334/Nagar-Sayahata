# Current System Flow

## 1. URL Routing

Main URL configuration in `config/urls.py`:
- `/admin` → `backend.apps.admin_auth.urls`
- `/admin/` → `backend.apps.admin_panel.urls`
- `/frontend/` → `frontend.apps.core.urls`
- `/` (root) → `frontend.apps.user_auth.urls`

## 2. Active Frontend Flow

### Home Page (Active Frontend)
- URL: `/frontend/navbar/` or root `/`
- View: `frontend.apps.core.views.Core`
- Template: `frontend/templates/core/index.html`
- CSS: `frontend/static/css/core/style.css`

### Navbar Structure
The home page navbar contains:
- **Home** - Active by default
- **About** - Information page
- **Municipality Search** - Search functionality
- **Public Statistics** - Public data display
- **Logout** - User logout action

### Navbar Features
- Responsive navbar with flexbox layout
- Brand logo on left ("Nagar Sahayata")
- Menu items aligned right
- Active state styling for current page
- Hover effects on menu items
- Dark theme navbar (#2c3e50 background)

## 3. Responsive Behavior

### Desktop (Default)
- Navbar displays horizontally
- Flex layout: justify-content: space-between
- Menu items have 1.5rem gap
- Padding: 0.5rem 1rem on links

### Mobile (CSS Media Query - implicit via flex wrap)
- Navbar maintains horizontal layout
- Content stacks on smaller screens
- No dedicated mobile hamburger menu toggle yet (CSS-only responsive)

## 4. Static File Loading

### Frontend Static Files
- Located at: `myproject/frontend/static/`
- CSS loaded via: `{% static 'css/core/style.css' %}`
- Configured in settings.py:
  ```python
  STATICFILES_DIRS = [
      BASE_DIR / "backend" / "static",
      BASE_DIR / "frontend" / "static",
  ]
  ```

### Template Loading
- Frontend templates at: `myproject/frontend/templates/`
- Configured in settings.py:
  ```python
  TEMPLATES = [{
      'DIRS': [
          BASE_DIR / "backend" / "templates",
          BASE_DIR / "frontend" / "templates",
      ],
  }]
  ```

## 5. Admin Panel Flow (Secondary)

### Admin Login
- URL: `/admin/login/`
- View: `backend.apps.admin_auth.views.LoginView`
- Template: `backend/templates/authentication/login.html`

### Admin Dashboard
- URL: `/admin/home/`
- View: `backend.apps.admin_panel.views.Home`
- Template: `backend/templates/home/home.html`
- Layout: `backend/templates/admin_panel.html`

## 6. Authentication Flow

### User Authentication (Frontend)
- Login page at root `/`
- Managed by `frontend.apps.user_auth`

### Admin Authentication (Backend)
- Login at `/admin/login/`
- Logout at `/admin/logout/`
- Managed by `backend.apps.admin_auth`

## 7. Database Configuration

- Engine: `django.db.backends.mysql`
- Database: `nagar_sahayata_db`
- User: `root`
- Password: `root`
- Host: `localhost`
- Port: `3306`

## 8. Notes

- Active frontend is in `myproject/frontend/`
- Root-level `frontend/` folder exists but is not used
- CSS static loading fixed by adding frontend static to STATICFILES_DIRS
- No mobile hamburger menu toggle yet (CSS-only responsive design)