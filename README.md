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
  ```bash
    git clone https://github.com/Pradi8/project.Quizly-backend  
  ```  
  ```bash 
    cd project.Quizly-backend
  ```

## 2. Create a virtual environment
  ```bash 
    python -m venv env
  ```

## 3. Activate the virtual environment
### <b>Linux/Mac</b>
```bash
  source env/bin/activate  
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

Download a Windows build from the official website:

```bash
  https://ffmpeg.org/download.html
```

or use a trusted build provider:

```bash
  https://www.gyan.dev/ffmpeg/builds/
```
Extract the downloaded archive

Move it to a location such as:

```bash
  C:\ffmpeg
```

After extraction, your folder should look like:

```bash
  C:\ffmpeg\bin
```

Add FFmpeg to PATH

Add the following path to your Windows environment variables:

```bash
  C:\ffmpeg\bin
```

Steps:

1. Open System Environment Variables
2. Click Environment Variables
3. Select Path under System Variables
4. Click Edit
5. Add:

```bash
  C:\ffmpeg\bin
```
6. Save and close all dialogs
7. Verify Installation
   Open a new terminal and run:
```bash
  ffmpeg -version
```

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

## Gemini Key

### 1. Get a Gemini API Key

This project requires a **Google Gemini API key**.

1. Go to https://aistudio.google.com/app/apikey
2. Sign in with your Google account
3. Click **Create API Key**
4. Copy your API key

---

### 2. Create a `.env` file

Create a `.env` file in the project root directory and add your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Notes

Make sure your `.env` file is not committed to Git. Add it to `.gitignore`:

```
gitignore.env
```

If the API key is missing or invalid, the application will not be able to connect to the Gemini API.

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