# Django ToDo API

## 📌 Overview

This project is a simple ToDo API built using Django and Django REST Framework.
It allows users to create, view, update, and delete tasks.

---

## 🚀 Features

* Create a task
* View all tasks
* Update a task
* Delete a task
* RESTful API implementation

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default database)

---

## 📂 Project Structure

```
todo_project/
│── todo/              # App containing models, views, serializers
│── todo_project/      # Project settings
│── manage.py
│── db.sqlite3
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/karthikavs-cse/django-todo-api.git
cd django-todo-api
```

### 2. Create virtual environment (optional)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install django djangorestframework
```

### 4. Run migrations

```
python manage.py migrate
```

### 5. Run server

```
python manage.py runserver
```

---

## 🌐 API Endpoints

### 🔹 Get all tasks

GET `/api/tasks/`

### 🔹 Create a task

POST `/api/tasks/`

### 🔹 Update a task

PUT `/api/tasks/<id>/`

### 🔹 Delete a task

DELETE `/api/tasks/<id>/`

---

## 📌 Example Request (POST)

```
{
  "title": "Learn Django",
  "description": "Build ToDo API",
  "completed": false
}
```

---

## 📌 Author

Karthika VS

---
