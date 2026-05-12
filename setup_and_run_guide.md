# Setup and Run Guide for Smart Municipal Grievance System

## 1. Project Setup Overview

The Smart Municipal Grievance System is a Django-based web application designed to facilitate the submission, tracking, and management of municipal grievances. It provides a platform for citizens to report issues and for administrators to manage and resolve them efficiently.

### Technologies Used
- **Python**: Programming language for backend development.
- **Django**: Web framework for building the application.
- **Database**: MariaDB/MySQL (with SQLite as a fallback for development).
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap for styling).
- **Additional Libraries**: Pillow for image handling, mysqlclient for database connectivity, python-dotenv for environment variables.

## 2. Virtual Environment Setup (myenv)

A virtual environment isolates the project's dependencies from the system-wide Python installation, preventing conflicts and ensuring reproducibility.

### Why Virtual Environment is Needed
Virtual environments allow different projects to use different versions of packages without interference. It keeps the global Python installation clean and ensures that dependencies are installed in a controlled environment.

### Creating the Virtual Environment
1. Ensure Python is installed on your system (version 3.8 or higher recommended).
2. Open a terminal or command prompt.
3. Navigate to the project root directory (where `requirements.txt` is located).
4. Run the following command to create a virtual environment named `myenv`:

   ```
   python -m venv myenv
   ```

### Activating the Virtual Environment
Activation loads the virtual environment's Python interpreter and packages.

#### On Windows (PowerShell):
```
myenv\Scripts\activate
```

#### On Windows (Command Prompt):
```
myenv\Scripts\activate.bat
```

#### On macOS/Linux or Git Bash:
```
source myenv/bin/activate
```

After activation, the command prompt will show `(myenv)` at the beginning, indicating the virtual environment is active.

### Installing Dependencies Inside the Virtual Environment
With the virtual environment activated, install the required packages using `pip`:

```
pip install -r requirements.txt
```

This installs all dependencies listed in `requirements.txt` into the virtual environment.

## 3. Project Installation Steps

### Cloning or Opening the Project Folder
1. If cloning from a repository (e.g., GitHub), use:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```
2. Alternatively, if the project folder is already available, navigate to it using the file explorer or terminal.

### Installing Requirements
1. Ensure the virtual environment is activated (see Section 2).
2. Run the following command to install all dependencies:
   ```
   pip install -r requirements.txt
   ```

### Verifying Installation
1. After installation, verify Django is installed by running:
   ```
   python -c "import django; print(django.get_version())"
   ```
2. Check other packages similarly if needed.

## 4. Running Django Project

All Django management commands must be executed from the directory containing `manage.py`, which is `myproject/`.

### Applying Migrations
Migrations synchronize the database schema with the models defined in the code.

1. Navigate to the `myproject/` directory:
   ```
   cd myproject
   ```
2. Generate migration files for any model changes:
   ```
   python manage.py makemigrations
   ```
3. Apply the migrations to the database:
   ```
   python manage.py migrate
   ```

### Running the Development Server
1. From the `myproject/` directory, start the server:
   ```
   python manage.py runserver
   ```
2. The server will start on `http://127.0.0.1:8000/` by default.
3. Open a web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## 5. Folder Execution Rules

### Main Project Folder
The main project folder is `myproject/`, which contains the Django project configuration and the `manage.py` script.

### Location of manage.py
`manage.py` is located in `myproject/manage.py`. This script is used to run Django commands.

### Execution Directory Rules
- All Django commands (e.g., `makemigrations`, `migrate`, `runserver`) must be run from the `myproject/` directory.
- Running commands outside this directory may result in errors, as Django cannot locate the project settings.
- Always ensure you are in the correct directory before executing commands.

## 6. Required Installations / Dependencies

The project requires the following packages, listed in `requirements.txt`:

- **Django**: Web framework (version 6.0.5 or compatible).
- **mysqlclient**: MySQL/MariaDB database connector (version 2.2.8).
- **Pillow**: Image processing library.
- **python-dotenv**: Environment variable management.

### Installing Dependencies
Install all dependencies at once using:
```
pip install -r requirements.txt
```

This ensures all required packages are installed in the virtual environment.

## 7. Database Setup

### Database Used
The project uses MariaDB/MySQL as the primary database. SQLite can be used as a fallback for development if MySQL is not available.

### Configuring DATABASES in settings.py
1. Open `myproject/config/settings.py`.
2. Locate the `DATABASES` dictionary.
3. For MySQL/MariaDB, configure as follows (replace with your credentials):
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
4. For SQLite (fallback):
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

### Creating Database Manually
If using MySQL/MariaDB, create the database manually in your MySQL client:
```
CREATE DATABASE your_database_name;
```

### Migrations and Database Flow
- **makemigrations**: Analyzes model changes and creates migration files that describe how to alter the database schema.
- **migrate**: Applies the migration files to the database, creating or modifying tables as needed.
- Basic Flow: Define models in `models.py` → Run `makemigrations` → Run `migrate` → Database schema is updated.

## 8. Common Issues & Fixes

### TemplateDoesNotExist Error
- **Cause**: Django cannot find the template files.
- **Fix**: Ensure templates are in `backend/templates/` and `TEMPLATES` in `settings.py` points to the correct directory. Run `python manage.py collectstatic` if needed.

### Module Not Found Error
- **Cause**: Required packages are not installed.
- **Fix**: Activate the virtual environment and run `pip install -r requirements.txt`. Ensure all dependencies are listed in `requirements.txt`.

### Static Files Not Loading
- **Cause**: Static files are not collected or served correctly.
- **Fix**: Run `python manage.py collectstatic` and ensure `STATIC_URL` and `STATIC_ROOT` are configured in `settings.py`. In development, ensure `DEBUG=True`.

### Database Connection Error
- **Cause**: Incorrect database configuration or database not running.
- **Fix**: Verify `DATABASES` settings in `settings.py`. Ensure the database server is running and credentials are correct. For MySQL, check if the database exists.

## 9. Final Checklist Before Running

- [ ] Virtual environment is activated (`myenv`).
- [ ] All dependencies are installed (`pip install -r requirements.txt`).
- [ ] Migrations are applied (`python manage.py migrate`).
- [ ] Database is configured in `settings.py`.
- [ ] Commands are run from the `myproject/` directory.
- [ ] Server starts without errors (`python manage.py runserver`).




