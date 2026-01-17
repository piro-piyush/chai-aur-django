# Chai Aur Django ☕🐍

A beginner-friendly Django project setup guide covering environment setup, project initialization, app creation, Tailwind CSS integration, and daily-use migration commands.

---

## 📝 Topics Covered

1. [Prerequisites](#1-prerequisites)
2. [Project Initialization](#2-project-initialization)
3. [Install Dependencies](#3-install-dependencies)
4. [Create Django Project](#4-create-django-project)
5. [Create Django App](#5-create-django-app)
6. [Register App](#6-register-app)
7. [Run Development Server](#7-run-development-server)
8. [Tailwind CSS Setup](#8-tailwind-css-setup)
9. [Enable Admin Panel](#9-enable-admin-panel)
10. [Migration Basics](#10-migration-basics)
11. [Common Commands Cheat Sheet](#11-common-commands-cheat-sheet)
12. [Next Steps](#12-next-steps)
13. [Credits](#13-credits)

---

## 📌 1. Prerequisites {#1-prerequisites}

Make sure you have the following installed:

* Python 3.10+
* pip (comes with Python)
* Virtual environment support
* Node.js & npm (for Tailwind with Node.js)

Check Python version:

```bash
python --version
```

---

## 🚀 2. Project Initialization {#2-project-initialization}

### 2.1 Create Virtual Environment

```bash
python -m venv .venv
```

### 2.2 Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

> You should see `(.venv)` in your terminal after activation.

---

## 📦 3. Install Dependencies {#3-install-dependencies}

### 3.1 Install Django

```bash
pip install django
```

### 3.2 Check Django Version

```bash
django-admin --version
```

### 3.3 Save Installed Packages

```bash
pip freeze > requirements.txt
```

### 3.4 Install From Requirements File

```bash
pip install -r requirements.txt
```

---

## 🏗️ 4. Create Django Project {#4-create-django-project}

```bash
django-admin startproject myproject
```

Project structure:

```
myproject/
├── manage.py
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 📂 5. Create Django App {#5-create-django-app}

```bash
cd myproject
python manage.py startapp myapp
```

App structure:

```
myapp/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── migrations/
```

---

## ⚙️ 6. Register App {#6-register-app}

Open `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'myapp',
]
```

---

## ▶️ 7. Run Development Server {#7-run-development-server}

```bash
python manage.py runserver
```

Open browser 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🎨 8. Tailwind CSS Setup {#8-tailwind-css-setup}

### 8.1 Install Packages

```bash
pip install django-tailwind[reload]
```

> If pip fails, upgrade it:

```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### 8.2 Initialize Tailwind App

```bash
python manage.py tailwind init
```

* Choose template:
  1️⃣ Standalone (no Node.js)
  2️⃣ Full (requires Node.js)
  3️⃣ Legacy v3

### 8.3 Update `settings.py`

```python
INSTALLED_APPS += ['tailwind', 'theme']
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"  # if using Node.js
```

### 8.4 Install Tailwind Dependencies

```bash
python manage.py tailwind install
```

### 8.5 Run Development Server & Tailwind

* First terminal:

```bash
python manage.py runserver
```

* Second terminal:

```bash
python manage.py tailwind start
```

> Hot reloading enabled with `django-tailwind[reload]`

### 8.6 Enable Browser Reload

```python
# settings.py
INSTALLED_APPS += ['django_browser_reload']
MIDDLEWARE += ['django_browser_reload.middleware.BrowserReloadMiddleware']
```

```python
# urls.py
from django.urls import include, path
urlpatterns += [path('__reload__/', include('django_browser_reload.urls'))]
```

---

## 🛠 9. Enable Admin Panel {#9-enable-admin-panel}

```bash
python manage.py migrate
python manage.py createsuperuser
```

* Access admin 👉 [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🧩 10. Migration Basics {#10-migration-basics}

### 10.1 Create Migrations

```bash
python manage.py makemigrations
```

### 10.2 Apply Migrations

```bash
python manage.py migrate
```

---

## ✅ 11. Common Commands Cheat Sheet {#11-common-commands-cheat-sheet}

```bash
python manage.py createsuperuser
python manage.py shell
python manage.py check
```

---

## 📚 12. Next Steps {#12-next-steps}

* Django Models & ORM
* URL Routing & Views
* Templates & Static Files
* Admin Customization
* Authentication & Authorization

---

## 💡 13. Credits {#13-credits}

Inspired by **Chai Aur Django** learning style ☕

Happy Coding! 🚀
