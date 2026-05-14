# Current System Flow

## 1. Current Authentication Flow

- Login page served by `backend.apps.authentication.views.LoginView`.
- URL paths:
  - `/login/` → `auth:login`
  - `/logout/` → `auth:logout`
- `LoginView.get()` renders `authentication/login.html`.
- If a user is already authenticated, login GET redirects to `admin_panel:home`.
- `LoginView.post()`:
  - checks lockout state via cache
  - validates username/password
  - uses `authenticate()` and `login()` from Django auth
  - on success, redirects to `/admin/home/` or `next` parameter if provided
  - on failure, records attempts and adds delay
- `LogoutView.get()` logs out the user and redirects to `/login/`.

## 2. Current Admin Panel Features

- `admin_panel.html` is the main admin layout template.
- Sidebar navigation for desktop with:
  - Home
  - About
  - Skills
  - Projects
  - Timeline
  - Contact
- Sidebar behavior:
  - desktop left sidebar remains
  - collapsed sidebar mode for desktop with compact logo
  - hover preview expands collapsed sidebar temporarily
- Mobile behavior:
  - bottom fixed navigation bar on screens <= 768px
  - horizontal nav items and touch-friendly layout
- Navbar features:
  - sidebar toggle button
  - theme toggle button
  - profile dropdown with My Profile and Logout
- Current JS logic in `backend/static/js/admin_panel/script.js` handles:
  - sidebar collapsed/expanded state
  - hover preview on desktop collapsed sidebar
  - responsive mobile state changes
  - theme toggle persistence
  - dropdown toggle behavior

## 3. Current Routing System

- `config/urls.py` routes:
  - root path `''` includes `backend.apps.authentication.urls`
  - `/admin/` includes `backend.apps.admin_panel.urls`
- `backend/apps/authentication/urls.py`:
  - `login/`
  - `logout/`
- `backend/apps/admin_panel/urls.py`:
  - `''` → `MainFunctionView` (admin landing page)
  - `home/` → `Home` view

## 4. Current Static System

- Static root folder: `myproject/backend/static`
- Admin panel assets:
  - `backend/static/css/admin_panel/style.css`
  - `backend/static/js/admin_panel/script.js`
- Home dashboard CSS:
  - `backend/static/css/home/home.css`
- Authentication login CSS:
  - `backend/static/css/authentication/login.css`
- Image/static handling uses Django `STATIC_URL` and `STATICFILES_DIRS`.
- Current static settings in `myproject/config/settings.py`:
  - `STATIC_URL = '/static/'`
  - `STATICFILES_DIRS = [BASE_DIR / 'backend' / 'static']`
  - `STATIC_ROOT = BASE_DIR / 'staticfiles'`
- Media settings:
  - `MEDIA_URL = '/media/'`
  - `MEDIA_ROOT = BASE_DIR / 'backend' / 'media'`

## 5. Current Template System

- Base layout for admin pages: `backend/templates/admin_panel.html`
- Dashboard page extends `admin_panel.html` using `{% extends 'admin_panel.html' %}`.
- Login page is `backend/templates/authentication/login.html` and does not extend the admin base.
- The admin panel uses template blocks:
  - `title`
  - `extra_css`
  - `content`
  - `extra_js`

## 6. Current Responsive Features

- Desktop:
  - left fixed sidebar at `var(--sidebar-width)`
  - content area pushed right by sidebar width
  - hover-expand behavior for collapsed sidebar
- Mobile/tablet:
  - sidebar converts to fixed bottom navigation
  - horizontal nav layout with equally spaced items
  - bottom nav padding prevents content overlap
  - mobile toggle button is hidden because bottom nav replaces left sidebar

## 7. Current Database Setup

- Database engine configured in `myproject/config/settings.py`:
  - `django.db.backends.mysql`
- Current connection values:
  - NAME: `nagar_sahayata_db`
  - USER: `root`
  - PASSWORD: `root`
  - HOST: `localhost`
  - PORT: `3306`
- Migration system is Django migrations.
- Current model status:
  - `backend/apps/authentication/models.py` defines a simple `User` model.
  - `backend/apps/admin_panel/models.py` is currently empty.
  - The login flow uses Django auth functions, not a custom `AUTH_USER_MODEL` in settings.

## 8. Current Security/System Logic

- Authentication checks use Django middleware and built-in auth functions.
- Login protection includes cache-based brute force tracking:
  - failed attempts recorded by IP address
  - lockout after 5 failed attempts
  - progressive delay on failures
- CSRF is enabled via Django middleware and `{% csrf_token %}` in forms.
- Logout clears session and redirects to login.

## 9. Current Existing Pages/Templates

- `authentication/login.html` — login/setup page
- `admin_panel.html` — admin panel shell/layout
- `home/home.html` — dashboard/home content page

## Notes

- No Django REST Framework or API endpoints are currently implemented.
- Current functionality is focused on Django template rendering and frontend UI behavior.

