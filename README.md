# 🗂️ Google Keep Server  
A lightweight and fast backend service for managing notes, inspired by Google Keep.

## 📌 About the Project
**Google Keep Server** is a Django REST Framework–based API that provides full note-management capabilities. It includes secure authentication, user management, labels, note archiving, trash handling, and search features. The backend is designed to easily integrate with web or mobile applications.

## ✨ Features
- 🔐 **JWT Authentication** (Access + Refresh Tokens)  
- 📝 **Full Notes CRUD** (create, edit, delete, archive)  
- 🏷️ **Label system** for organizing notes  
- 👤 **User registration, login, and password change**  
- 📄 **API documentation with Swagger**  
- 🧱 Clean, modular, and extensible architecture

## 🛠️ Technologies
- Python  
- Django / Django REST Framework  
- PostgreSQL  

## 📦 Quick Start
```bash
git clone https://github.com/your-repo/google-keep-server.git
cd google-keep-server
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
