# Quizly API

## Overview
Quizly is an AI-powered quiz application built with the **Django REST Framework**. Users can paste the URL of a YouTube video, after which the app automatically generates a summary of the video and creates a quiz with 10 questions using artificial intelligence. 
Authentication is handled using JWT (JSON Web Tokens) and HTTP-only cookies to ensure secure management of user data.
---

## Features
- User registration, login, and logout
- CRUD operations for **Offers** , **Orders** and **Reviews**
- Reviews system for oders, offers
- Object-level permissions:
  - Only authors can edit their reviews
  - Only admins or authors can delete reviews
- Token-based authentication
- Browsable API for development

---

# Installation
## Follow these steps to set up the project locally:

## Requirements: Python 3.12

## 1. Clone the repository
  git clone https://github.com/Pradi8/project.Quizly-backend <br>   
  cd Quizly-backend

## 2. Create a virtual environment
  ```bash 
    python -m venv env
  ```

## 3. Activate the virtual environment
### <b>Linux/Mac</b>
```bash
  env/bin/activate  
```
### <b>Windows</b>
```bash
  env\Scripts\activate      
```

## 4. Install Python dependencies
```bash
  python -m pip install -r requirements.txt
```


sudo apt update
sudo apt install ffmpeg

## 🐧 Redis Installation

### WSL / Linux (Ubuntu)

```bash
nicht in env modus !
sudo apt update
sudo apt install redis-server

redis-server

mac os:
brew install redis
redis-server

windows:
pip install redis



## 5. Create database migrations
```bash
  python manage.py makemigrations
```

## 6. Apply database migrations
```bash
  python manage.py migrate
```

## 7. Create a superuser (admin account)
```bash
  python manage.py createsuperuser
```

## 8. Start the development server
```bash
  python manage.py runserver  
```
  The project will be running at http://127.0.0.1:8000/


# Project Structure
## quizly_app/
├── models.py        # Offer, Offerdetails <br>
├── views.py         # API views  <br>
├── paginations.py   # API paginations  <br>
├── filters.py       # DRF filters  <br>
├── serializers.py   # DRF serializers  <br>
├── urls.py

## auth_app/
├── models.py        # Customuser, Fileupload  <br>
├── views.py         # Registration, login, logout  <br>
├── serializers.py   # DRF serializers  <br>
├── urls.py  <br>
├── permissions.py   # Custom permissions

manage.py
requirements.txt
README.md