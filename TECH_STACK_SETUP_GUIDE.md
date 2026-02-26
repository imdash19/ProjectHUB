📋 HOW TO LOAD TECH STACKS & SEE THEM IN ADD PROJECT FORM

================================================================================================
IMPORTANT: Tech Stacks Must Be Loaded BEFORE You See Them in the Add Project Form!
================================================================================================

STEP 1: VERIFY DATABASE IS CREATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run migrations first:
```bash
python manage.py makemigrations
python manage.py migrate
```

STEP 2: CREATE SUPERUSER (IF NOT ALREADY DONE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```bash
python manage.py createsuperuser
```

Answer the prompts:
- Username: admin
- Email: admin@example.com
- Password: (choose a secure password)
- Confirm Password: (repeat password)

STEP 3: LOAD TECH STACKS
━━━━━━━━━━━━━━━━━━━━━━━━━

Open Django shell:
```bash
python manage.py shell
```

Copy and paste this script:
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
    {'name': 'Node.js', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/919/919825.png', 'color': '#68a063'},
    {'name': 'TypeScript', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/919/919830.png', 'color': '#3178c6'},
    {'name': 'AWS', 'logo_url': 'https://cdn-icons-png.flaticon.com/512/919/919853.png', 'color': '#FF9900'},
]

for tech in techs:
    TechStack.objects.get_or_create(
        name=tech['name'],
        defaults={
            'logo_url': tech['logo_url'],
            'color': tech['color']
        }
    )
    print(f"✅ Created/Updated: {tech['name']}")

print(f"\n✅ Total tech stacks: {TechStack.objects.count()}")
exit()
```

Expected output:
```
✅ Created/Updated: Python
✅ Created/Updated: Django
✅ Created/Updated: JavaScript
...
✅ Total tech stacks: 15
```

STEP 4: VERIFY TECH STACKS LOADED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Option A: Via Django Shell
```bash
python manage.py shell
```
```python
from testapp.models import TechStack
techs = TechStack.objects.all()
print(f"Total: {techs.count()}")
for tech in techs:
    print(f"  - {tech.name} ({tech.logo_url})")
exit()
```

Option B: Via Admin Panel
1. Start server: `python manage.py runserver`
2. Go to http://localhost:8000/admin/
3. Login with superuser credentials
4. Click on "Tech Stacks"
5. You should see all 15 technologies listed

STEP 5: NOW CREATE A PROJECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Go to http://localhost:8000/register/ and create an account
2. OR login with an existing account
3. Go to Dashboard
4. Click "➕ New Project"
5. Fill in project details:
   - Project Name: (e.g., "My Portfolio Website")
   - Description: (e.g., "A beautiful portfolio built with Django")
6. **YOU SHOULD NOW SEE TECH STACK OPTIONS WITH LOGOS!**
   - Each technology shows with its logo
   - Click to select multiple
   - Blue highlight when selected
7. Add GitHub and Live links (optional)
8. Click "Create Project"
9. Go back to dashboard and see your project with tech badges!

TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ PROBLEM: I don't see tech stack options in the Add Project form

✅ SOLUTION 1: Tech stacks might not be loaded
   □ Open Django shell: python manage.py shell
   □ Run: from testapp.models import TechStack
   □ Run: print(TechStack.objects.count())
   □ If output is 0, load tech stacks using the script above

✅ SOLUTION 2: Database not migrated
   □ Run: python manage.py migrate
   □ Then load tech stacks again

✅ SOLUTION 3: Clear browser cache
   □ Hard refresh: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)
   □ Try again

✅ SOLUTION 4: Check server is running
   □ Make sure: python manage.py runserver
   □ No errors in console?

❌ PROBLEM: Logos are not showing (showing ⚙️ instead)

✅ SOLUTION 1: Image URLs are broken
   □ Go to /admin/
   □ Click TechStack
   □ Check logo_url for each tech
   □ Update with correct CDN URLs if needed

✅ SOLUTION 2: Internet connectivity
   □ Logos are loaded from CDN (flaticon.com)
   □ Make sure you have internet connection

✅ SOLUTION 3: Use offline logos
   □ Instead of URLs, upload logo images locally
   □ Update tech stack with local image paths

❌ PROBLEM: "No tech stacks available" message

✅ SOLUTION: Load tech stacks first!
   □ Follow STEP 3 above
   □ Make sure script runs without errors
   □ Verify count: TechStack.objects.count()
   □ Should be 15 (or however many you loaded)

❌ PROBLEM: Selected tech stacks don't save

✅ SOLUTION: Check form submission
   □ Make sure form method is POST
   □ Check for form errors on page
   □ Look at browser console for JavaScript errors
   □ Check server console for error messages

QUICK VERIFICATION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before accessing Add Project form:
☑ Database migrations run: python manage.py migrate
☑ Superuser created: python manage.py createsuperuser
☑ Tech stacks loaded: python manage.py shell → [run script]
☑ Server running: python manage.py runserver
☑ You're logged in to application
☑ Browser cache cleared (Ctrl+Shift+R)

Expected behavior:
☑ Go to Add Project page
☑ See "🔧 Technology Stack (Click to Select)"
☑ See grid of 15+ technology options
☑ Each option shows logo + name
☑ Click to toggle selection (blue highlight)
☑ Create project with selected techs
☑ Return to dashboard
☑ See project card with tech badges

ALTERNATIVE: Add Tech Stacks Via Admin
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

If you prefer to add tech stacks manually:

1. Start server: python manage.py runserver
2. Go to http://localhost:8000/admin/
3. Login with superuser
4. Click "+ Add" next to "Tech Stacks"
5. Fill in:
   - Name: (e.g., "Python")
   - Logo URL: (paste CDN URL)
   - Color: (HEX color like #3776ab)
6. Click "Save"
7. Repeat for each technology
8. Refresh Add Project form
9. You should see all added tech stacks

Useful CDN URLs for logos:
- Python: https://cdn-icons-png.flaticon.com/512/5891/5891069.png
- Django: https://static.djangoproject.com/img/icon-touch.e4872c4da332.png
- JavaScript: https://cdn-icons-png.flaticon.com/512/5968/5968292.png
- React: https://cdn-icons-png.flaticon.com/512/919/919851.png
- Vue: https://cdn-icons-png.flaticon.com/512/919/919828.png
- Node.js: https://cdn-icons-png.flaticon.com/512/919/919825.png
(See full list in SETUP_INSTRUCTIONS.md)

WHAT'S HAPPENING BEHIND THE SCENES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

When you load tech stacks:
1. Script creates TechStack objects in database
2. Each TechStack has name, logo_url, color
3. Stored in testapp_techstack table

When you access Add Project form:
1. View queries: TechStack.objects.all()
2. Passes to template as: tech_stacks variable
3. Template loops through and displays each
4. Each shows logo (from logo_url) + name
5. Each has checkbox with unique ID
6. Selected checkboxes on form submission create M2M relationships

When you select techs and save:
1. Form validates input
2. Project created
3. form.save_m2m() creates ManyToMany relationships
4. Tech badges now show on project card in dashboard

NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ✅ Load tech stacks (follow STEP 3)
2. ✅ Create a test project with techs selected
3. ✅ See project with tech badges in dashboard
4. ✅ Edit project to change/add techs
5. ✅ Delete test project
6. ✅ Generate API token
7. ✅ Test API endpoint with token
8. ✅ Deploy to production!

Questions? Check:
- SETUP_INSTRUCTIONS.md
- API_USAGE_GUIDE.md
- QUICK_REFERENCE.md

Happy coding! 🚀
