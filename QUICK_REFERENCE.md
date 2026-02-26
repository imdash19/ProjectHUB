# 🚀 Portfolio Hub - Quick Start Reference

## Initial Setup Commands

```bash
# 1. Create project directory
mkdir projecthub
cd projecthub

# 2. Create Django project
django-admin startproject projecthub .

# 3. Create app
python manage.py startapp testapp

# 4. Install dependencies
pip install -r requirements.txt

# 5. Copy all files to appropriate locations
# See file structure below

# 6. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 7. Create superuser (admin)
python manage.py createsuperuser

# 8. Load tech stacks (see SETUP_INSTRUCTIONS.md for details)
python manage.py shell
# Then run the tech stack loading code

# 9. Run development server
python manage.py runserver

# Now visit: http://localhost:8000
```

---

## 📁 File Structure & Placement

```
projecthub/
│
├── projecthub/
│   ├── __init__.py
│   ├── settings.py          ← REPLACE with provided settings.py
│   ├── urls.py              ← REPLACE with provided urls_projecthub.py
│   ├── asgi.py
│   └── wsgi.py
│
├── testapp/
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── templates/testapp/
│   │   ├── base.html                ← base.html
│   │   ├── login.html               ← login.html
│   │   ├── register.html            ← register.html
│   │   ├── dashboard.html           ← dashboard.html
│   │   ├── project_form.html        ← project_form.html
│   │   ├── generate_token.html      ← generate_token.html
│   │   └── token_success.html       ← token_success.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css            ← style.css
│   │   │   └── animations.css       ← (included in style.css)
│   │   └── js/
│   │       └── main.js              ← main.js
│   │
│   ├── __init__.py
│   ├── admin.py                     ← admin.py
│   ├── apps.py
│   ├── forms.py                     ← forms.py
│   ├── models.py                    ← models.py
│   ├── serializers.py               ← serializers.py
│   ├── views.py                     ← views.py
│   ├── urls.py                      ← urls_testapp.py (rename to urls.py)
│   └── tests.py
│
├── manage.py
└── requirements.txt                 ← requirements.txt
```

---

## File Download Guide

### Core Files (Required)
- ✅ `settings.py` → `projecthub/settings.py`
- ✅ `urls_projecthub.py` → `projecthub/urls.py`
- ✅ `urls_testapp.py` → `testapp/urls.py`
- ✅ `models.py` → `testapp/models.py`
- ✅ `views.py` → `testapp/views.py`
- ✅ `forms.py` → `testapp/forms.py`
- ✅ `serializers.py` → `testapp/serializers.py`
- ✅ `admin.py` → `testapp/admin.py`
- ✅ `requirements.txt` → `./requirements.txt`

### Templates (Required)
- ✅ `base.html` → `testapp/templates/testapp/base.html`
- ✅ `login.html` → `testapp/templates/testapp/login.html`
- ✅ `register.html` → `testapp/templates/testapp/register.html`
- ✅ `dashboard.html` → `testapp/templates/testapp/dashboard.html`
- ✅ `project_form.html` → `testapp/templates/testapp/project_form.html`
- ✅ `generate_token.html` → `testapp/templates/testapp/generate_token.html`
- ✅ `token_success.html` → `testapp/templates/testapp/token_success.html`

### Static Files (Required)
- ✅ `style.css` → `testapp/static/css/style.css`
- ✅ `main.js` → `testapp/static/js/main.js`

---

## 🎯 Key Routes

| Route | Purpose |
|-------|---------|
| `/` | Redirect to login/dashboard |
| `/login/` | Login page |
| `/register/` | Registration page |
| `/logout/` | Logout |
| `/dashboard/` | Main dashboard |
| `/project/add/` | Add new project |
| `/project/<id>/edit/` | Edit project |
| `/project/<id>/delete/` | Delete project |
| `/generate-token/` | Generate API token |
| `/api/health/` | API health check |
| `/api/user/<user_id>/projects/` | **Get all projects (API)** |
| `/admin/` | Django admin panel |

---

## 🔐 Authentication Flow

```
User Registration
    ↓
Automatic API Token Creation
    ↓
User Login
    ↓
Dashboard Access
    ↓
Optional: Regenerate Token
    ↓
Use Token for API Access
```

---

## 📊 Database Models

### TechStack
```python
- id (PK)
- name (CharField, unique)
- logo_url (URLField)
- color (CharField, HEX)
```

### Project
```python
- id (PK)
- user (FK to User)
- name (CharField)
- description (TextField)
- tech_stack (ManyToMany)
- github_link (URLField, optional)
- live_link (URLField, optional)
- created_at (DateTimeField, auto)
- updated_at (DateTimeField, auto)
```

### APIToken
```python
- id (PK)
- user (OneToOne)
- token (CharField, unique)
- created_at (DateTimeField, auto)
- regenerated_at (DateTimeField, optional)
- is_active (BooleanField)
```

---

## 🛠️ Useful Django Commands

```bash
# Create migrations for changes
python manage.py makemigrations testapp

# Apply migrations to database
python manage.py migrate

# Create superuser for admin
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Collect static files (production)
python manage.py collectstatic

# Clear database (development only!)
rm db.sqlite3
python manage.py migrate

# Run on different port
python manage.py runserver 8001

# Check for errors
python manage.py check

# Create app
python manage.py startapp appname
```

---

## 🐍 Python Shell - Loading Tech Stacks

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
        defaults={'logo_url': tech['logo_url'], 'color': tech['color']}
    )

print("✅ Tech stacks loaded!")
exit()
```

---

## 🧪 Testing the API

### Using cURL
```bash
curl -X GET "http://localhost:8000/api/user/1/projects/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### Health Check
```bash
curl http://localhost:8000/api/health/
```

---

## 🎨 Customization

### Change Primary Color
In `style.css`, update:
```css
:root {
    --primary: #6366f1;  ← Change this
    /* ... */
}
```

### Change App Name
In templates, replace "Portfolio Hub" with your app name

### Add More Tech Stacks
In admin panel or Python shell, create new `TechStack` objects

---

## 🚨 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `Port 8000 already in use` | Run `python manage.py runserver 8001` |
| `No such table: testapp_project` | Run `python manage.py migrate` |
| `Static files not loading` | Run `python manage.py collectstatic` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `CSRF token missing` | Check `{% csrf_token %}` in forms |
| `Template not found` | Check template directory structure |
| `No migrations for 'testapp'` | Run `python manage.py makemigrations testapp` |

---

## 📈 Deployment Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Add production domain to `ALLOWED_HOSTS`
- [ ] Change `SECRET_KEY` to a secure value
- [ ] Use MySQL instead of SQLite
- [ ] Set up HTTPS
- [ ] Configure STATIC_URL and MEDIA_URL
- [ ] Set up environment variables
- [ ] Run `python manage.py collectstatic`
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Configure reverse proxy (Nginx, Apache)

---

## 📚 Additional Resources

- 📖 [Django Documentation](https://docs.djangoproject.com/)
- 📖 [Django REST Framework](https://www.django-rest-framework.org/)
- 📖 [Python Documentation](https://docs.python.org/3/)
- 🎓 [Django for Beginners](https://djangoforbeginners.com/)

---

## 💡 Pro Tips

1. **Use `python manage.py shell_plus`** (from `django-extensions`) for better shell experience
2. **Use `django-debug-toolbar`** for development debugging
3. **Use `black`** for code formatting
4. **Use `flake8`** for code linting
5. **Use `.env` files** with `python-decouple` for secrets
6. **Use virtual environments** to isolate dependencies

---

## 🤝 Contributing

Feel free to customize and extend this application!

---

**Last Updated:** January 2024  
**Version:** 1.0
