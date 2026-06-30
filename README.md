# 📒 Phonebook Web Application (Django + MySQL)

A simple backend project built with Django for managing contacts using CRUD operations with MySQL database.

---

## 🚀 Features

- Add contacts
- Edit contacts
- Delete contacts
- Search contacts
- View all contacts

---

## 🛠 Tech Stack

- Python 3
- Django
- MySQL
- HTML / CSS

---

## 🗄 Database

MySQL is used as the database.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
