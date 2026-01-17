# Chai Aur Django ☕🐍

A beginner-friendly Django project setup guide covering environment setup, project initialization, app creation, and daily-use migration commands. Perfect for learning Django the right way.

---

## 📌 Prerequisites

Make sure you have the following installed:

* Python 3.10+
* pip (comes with Python)
* Virtual environment support

Check Python version:

```bash
python --version
```

---

## 🚀 Project Initialization

### 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 2️⃣ Activate Virtual Environment

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

## 📦 Install Dependencies

### Install Django

```bash
pip install django
```

### Check Django Version

```bash
django-admin --version
```

### Save Installed Packages

```bash
pip freeze > requirements.txt
```

### Install From Requirements File

```bash
pip install -r requirements.txt
```

---

## 🏗️ Create Django Project

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

## 📂 Create Django App

Move into project directory:

```bash
cd myproject
```

Create app:

```bash
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

## ⚙️ Register App in Project

Open `settings.py` and add your app:

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

## ▶️ Run Development Server

```bash
python manage.py runserver
```

Open browser:

👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧩 Migration Basics (Daily Use)

Whenever you change models:

### Create Migrations

```bash
python manage.py makemigrations
```

### Apply Migrations

```bash
python manage.py migrate
```

---

## ✅ Common Commands Cheat Sheet

```bash
python manage.py createsuperuser
python manage.py shell
python manage.py check
```

---

## 📚 Next Steps

* Learn Django Models & ORM
* URL Routing & Views
* Templates & Static Files
* Django Admin Customization
* Authentication & Authorization

---

## 💡 Credits

Inspired by **Chai Aur Django** learning style ☕

Happy Coding! 🚀
