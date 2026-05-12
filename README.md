# Quizly API

## Overview
Quizly is an AI-powered quiz application built with the **Django REST Framework**. Users can paste the URL of a YouTube video, after which the app automatically generates a summary of the video and creates a quiz with 10 questions using artificial intelligence. 
Authentication is handled using JWT (JSON Web Tokens) and HTTP-only cookies to ensure secure management of user data.

---

## Features
- User registration, login, and logout
- CRUD operations for quizzes (title, description)
- Automatic quiz generation from YouTube videos
- AI-powered question generation
- Object-level permissions
- JWT-based authentication
- Browsable API for development

---

## Installation

### Requirements
- Python 3.12
- ffmpeg
- yt-dlp

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

## 5. Install system dependencies

#### Install yt-dlp:

```bash
    pip install yt-dlp
```

### WSL / Linux (Ubuntu)

#### Install FFmpeg

```bash
  sudo apt update
  sudo apt install ffmpeg
```

#### Install Deno

```bash
    curl -fsSL https://deno.land/install.sh | sh
```

### Windows

#### Install FFmpeg

Download

```bash
  https://ffmpeg.org/download.html
```
Extract to e.g. C:\ffmpeg

Add to PATH: C:\ffmpeg\bin

#### Install Deno

```bash
    powershell -c "irm https://deno.land/install.ps1 | iex"
```

### Mac OS

##### install Homebrew

```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Install FFmpeg

```bash
   brew install ffmpeg
```
#### Install Deno

```bash
   brew install deno
```

## 6. Create database migrations
```bash
  python manage.py makemigrations
```

## 7. Apply database migrations
```bash
  python manage.py migrate
```

## 8. Create a superuser (admin account)
```bash
  python manage.py createsuperuser
```

## 9. Start the development server
```bash
  python manage.py runserver  
```
  The project will be running at http://127.0.0.1:8000/


# Project Structure
```
auth_app/
├── api/
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── permissions.py
quizly_app/
├── models.py
├── api/
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── services/
│   ├── ai_service.py
│   ├── audio_service.py
│   └── youtube_service.py
├── standardurl.py
├── tasks.py

core/
├── settings.py

manage.py <br>
requirements.txt <br>
README.md

```