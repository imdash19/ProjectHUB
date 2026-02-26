# Portfolio Hub - Complete Setup Guide

## 📋 Prerequisites
- Python 3.8+
- pip (Python package manager)
- MySQL Server (or use SQLite for development)
- Git (optional)

---

## 🚀 Step-by-Step Setup Instructions

### Step 1: Create Django Project
```bash
# Create project directory
mkdir projecthub
cd projecthub

# Create Django project
django-admin startproject projecthub .

# Create Django app
python manage.py startapp testapp
```

### Step 2: Install Dependencies
```bash
# Create requirements.txt and install
pip install Django==4.2.10
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install mysqlclient==2.2.0
pip install python-decouple==3.8
```

Or create `requirements.txt` and run:
```bash
pip install -r requirements.txt
```

### Step 3: Update Django Settings
Replace the content of `projecthub/settings.py` with the provided `settings.py` file.

### Step 4: Update URL Configuration
Replace `projecthub/urls.py` with the provided main `urls.py` file.
Replace `testapp/urls.py` with the provided app `urls.py` file.

### Step 5: Copy App Files
Copy these files to the `testapp` directory:
- `models.py`
- `views.py`
- `forms.py`
- `serializers.py`
- `urls.py`
- `admin.py`

### Step 6: Create Template Directory
```bash
# Create templates directory
mkdir -p testapp/templates/testapp
mkdir -p testapp/static/css
mkdir -p testapp/static/js
mkdir -p testapp/static/images
```

### Step 7: Copy Templates and Static Files
Copy HTML files to `testapp/templates/testapp/`
Copy CSS files to `testapp/static/css/`
Copy JavaScript files to `testapp/static/js/`

### Step 8: Apply Migrations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

### Step 9: Create Superuser (Admin)
```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

### Step 10: Load Initial Data (Tech Stack)
```bash
# Create initial tech stacks via Django shell
python manage.py shell
```

Then run in the shell:
```python
from testapp.models import TechStack

techs = [
    {'name': 'Python', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/5891/5891069.png', 'color': '#3776ab'},
    {'name': 'Django', 'logo_url': 'https://static.djangoproject.com/img/icon-touch.e4872c4da332.png', 'color': '#092e20'},
    {'name': 'JavaScript', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/5968/5968292.png', 'color': '#f7df1e'},
    {'name': 'React', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/919/919851.png', 'color': '#61dafb'},
    {'name': 'HTML5', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/1199/1199519.png', 'color': '#e34c26'},
    {'name': 'CSS3', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/732/732190.png', 'color': '#1572b6'},
    {'name': 'MySQL', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/919/919836.png', 'color': '#00758f'},
    {'name': 'Docker', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/919/919853.png', 'color': '#2496ed'},
    {'name': 'Vue.js', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/919/919828.png', 'color': '#42b883'},
    {'name': 'PostgreSQL', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/4248/4248443.png', 'color': '#336791'},
    {'name': 'Git', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/2111/2111432.png', 'color': '#f1502f'},
    {'name': 'MongoDB', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/4248/4248440.png', 'color': '#13aa52'},
]

for tech in techs:
    TechStack.objects.get_or_create(
        name=tech['name'],
        defaults={
            'logo_url': tech['logo_url'],
            'color': tech['color']
        }
    )

print("Tech stacks loaded successfully!")
exit()
```

### Step 11: Run Development Server
```bash
python manage.py runserver
```

The application will be available at:
- **Web App**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

---

## 🔐 MySQL Configuration (Optional)

If you want to use MySQL instead of SQLite:

### 1. Create Database
```sql
CREATE DATABASE portfolio_db;
CREATE USER 'portfolio_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON portfolio_db.* TO 'portfolio_user'@'localhost';
FLUSH PRIVILEGES;
```

### 2. Update Settings
In `projecthub/settings.py`, uncomment and modify:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'portfolio_db',
        'USER': 'portfolio_user',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3. Install MySQL Driver
```bash
pip install mysqlclient
```

---

## 📁 Project Structure

```
projecthub/
├── projecthub/
│   ├── __init__.py
│   ├── settings.py          ← Update with provided file
│   ├── urls.py              ← Update with provided file
│   ├── asgi.py
│   └── wsgi.py
├── testapp/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── testapp/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── project_form.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── token_success.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── animations.css
│   │   └── js/
│   │       └── main.js
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py             ← Add provided file
│   ├── models.py            ← Replace with provided file
│   ├── serializers.py       ← Add provided file
│   ├── views.py             ← Replace with provided file
│   ├── urls.py              ← Add provided file
│   └── tests.py
├── manage.py
└── requirements.txt         ← Add provided file
```

---

## 🎯 Key Features

### Authentication
- ✅ User Registration with email
- ✅ Secure Login/Logout
- ✅ Password hashing (Django default)
- ✅ Session management

### Project Management
- ✅ Create projects
- ✅ Edit projects
- ✅ Delete projects
- ✅ Multi-select tech stack with logos
- ✅ GitHub and Live links

### API Features
- ✅ Token-based authentication
- ✅ Secure API token generation
- ✅ Regenerate tokens
- ✅ Single endpoint: `/api/user/<userid>/projects/`

### UI/UX
- ✅ Modern SaaS design
- ✅ Glassmorphism effects
- ✅ Responsive (mobile, tablet, desktop)
- ✅ Smooth animations
- ✅ Dark mode ready

---

## 🔗 API Usage

### Generate Token
1. Login to your account
2. Go to Dashboard
3. Click "Generate API Token"
4. Verify with your password
5. Copy your token

### Use API
```bash
# Example API call
curl -X GET http://localhost:8000/api/user/1/projects/ \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

---

## 🐛 Troubleshooting

### Migration Errors
```bash
python manage.py makemigrations testapp
python manage.py migrate testapp
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Database Lock Error
```bash
rm db.sqlite3
python manage.py migrate
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

---

## 📚 Resources
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Python Official Docs](https://docs.python.org/3/)

---

## 🎉 Next Steps
1. ✅ Setup complete
2. ✅ Create admin account
3. ✅ Load tech stacks
4. ✅ Register test user
5. ✅ Create test project
6. ✅ Generate API token
7. ✅ Test API endpoint

Happy coding! 🚀
