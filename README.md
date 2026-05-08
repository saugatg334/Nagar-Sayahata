# 🏙️ Nagar Sahayata - Smart Municipal Grievance System

A Django-based digital grievance management platform for citizens to report and track municipal issues.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 6.0+
- MySQL or SQLite

### Setup
```bash
# Create virtual environment
python -m venv myenv
.\myenv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run migrations
cd myproject
python manage.py migrate

# Start server
python manage.py runserver
```

Access: `http://localhost:8000/`

## 📂 Project Structure

See [project_structure.md](project_structure.md) for detailed directory layout and URL routing.

## ✅ Key Features

### Authentication System
- User login with brute force protection
- Secure logout with session clearing
- Namespaced URL routing

### Admin Panel
- Dashboard for grievance management
- Real-time complaint tracking
- Municipality-based routing

### Database
- SQLite (development)
- MySQL (production)

## 🔧 Configuration

### Settings Location
`myproject/config/settings.py`

### Installed Apps
- `backend.apps.admin_pannel`
- `backend.apps.authentication`
- Django built-in apps (admin, auth, etc.)

### Database Setup
```bash
# Create superuser
python manage.py createsuperuser

# Access admin
http://localhost:8000/admin/
```

## 📝 URL Patterns

### Authentication Routes
- `/auth/login/` - User login page
- `/auth/logout/` - User logout (redirects to login)

### Admin Panel Routes
- `/` - Main dashboard
- `/home/` - Home section

## 🐛 Common Issues & Solutions

### NoReverseMatch Error
**Issue**: Django can't find URL name
**Solution**: Ensure `app_name` is defined in app's `urls.py` and use namespaced URLs in code

**Correct Usage**:
```python
# In views
redirect('auth:login')

# In templates
{% url 'auth:logout' %}

# In Python
reverse('admin_pannel:home')
```

### Database Connection Error
**Solution**: Check MySQL is running and credentials in `settings.py`

## 📁 File Structure

```
myproject/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── backend/
    ├── apps/
    │   ├── authentication/
    │   │   ├── urls.py (app_name = 'auth')
    │   │   └── views.py
    │   │
    │   └── admin_pannel/
    │       ├── urls.py (app_name = 'admin_pannel')
    │       └── views.py
    │
    ├── static/
    ├── media/
    └── templates/
```

## 🔑 Important Notes

1. **Virtual Environment**: Always activate before running Django commands
2. **Migrations**: Run `python manage.py migrate` after changes to models
3. **Namespace URLs**: Use `'app:name'` format in all URL references
4. **Static Files**: Collect with `python manage.py collectstatic` for production

## 📦 Dependencies

Core packages (see `requirements.txt`):
- Django 6.0+
- MySQLdb 2.2+
- Pillow 12.2+
- Python-dotenv 1.2+
- SQLparse 0.5+

## 🚀 Deployment

For production:
1. Update `settings.py` (DEBUG=False, allowed hosts)
2. Use environment variables for secrets
3. Set up MySQL database
4. Run `python manage.py collectstatic`
5. Use WSGI server (Gunicorn, uWSGI)
6. Set up reverse proxy (Nginx)

## 📞 Troubleshooting

**Server won't start?**
```bash
python manage.py check
python manage.py migrate
```

**Missing static files?**
```bash
python manage.py collectstatic --noinput
```

**Database errors?**
```bash
python manage.py flush  # Clear database
python manage.py migrate
```

## 📋 Next Steps

1. Create models in respective apps
2. Implement complaint submission form
3. Set up complaint tracking system
4. Add municipality management
5. Implement analytics/reporting


### 📌 Smart Complaint Submission
- User selects exact location using map pin
- Upload image/video proof of issue
- Complaint is directly assigned to responsible municipal staff
- Staff verifies and updates complaint status

---

### 🔄 Complaint Status Tracking
Users can track complaints in real-time:
- Pending
- In Progress
- Completed

---

### 👥 User Interaction Flow
- If user responds → system continues based on feedback
- If no response → staff continues handling complaint
- If complaint is fake → marked invalid with reason
- If no user response → auto-close system
- Reopen option available if needed

---

### 🏛️ Municipality Dashboard
Municipal staff can:
- View complaints by their municipality only
- Track total / pending / in-progress / completed complaints
- Identify high-issue areas
- Improve planning and decision making

---

### 🌍 Public Transparency View
Any user can:
- Search municipality
- View:
  - Total complaints
  - Pending cases
  - Completed cases
  - Ongoing work

👉 This increases transparency and accountability.

---

## 🔧 Technology Stack
- Frontend: HTML, CSS, Bootstrap, JavaScript
- Backend: Python (Django)
- Database: MySQL / MariaDB

---

## 💡 Future Enhancements
- AI Chatbot for complaint assistance
- Automatic complaint categorization
- Mobile application (Android/iOS)
- Emergency service integration (Police, Fire, Ambulance)
- AI-based priority detection (Urgent / Medium / Low)
- Image-based issue detection
- Advanced analytics dashboard
- Offline complaint submission support

---

## 🚀 Expected Benefits
- Faster complaint resolution
- Transparent system for citizens
- Reduced fake complaints
- Improved municipal performance tracking
- Better urban management
- Increased citizen trust

---

## 👨‍💻 Developer Note
This project is designed as a smart digital solution to modernize municipal grievance handling systems and improve public service delivery.



