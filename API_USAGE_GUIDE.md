# Portfolio Hub - API Usage Guide

## 📚 Table of Contents
1. [API Overview](#overview)
2. [Authentication](#authentication)
3. [Endpoints](#endpoints)
4. [Examples](#examples)
5. [Error Handling](#error-handling)
6. [Rate Limiting](#rate-limiting)

---

## Overview

The Portfolio Hub API allows you to programmatically access your projects. It's a simple RESTful API that returns JSON data.

**Base URL:** `http://localhost:8000`

**Current Version:** v1

---

## Authentication

### Token Generation

1. **Login** to your Portfolio Hub account
2. **Go to** Dashboard → API Access section
3. **Click** "Generate API Token"
4. **Verify** your credentials
5. **Copy** your token and keep it safe

### Using Your Token

All API requests require authentication via the `Authorization` header.

**Header Format:**
```
Authorization: Bearer YOUR_TOKEN_HERE
```

Or alternatively:
```
Authorization: Token YOUR_TOKEN_HERE
```

---

## Endpoints

### 1. Get User Projects

**Endpoint:** `GET /api/user/<user_id>/projects/`

**Authentication:** Required (Bearer Token)

**Parameters:**
- `user_id` (path): Your user ID (found in dashboard)

**Response:**
```json
{
    "status": "success",
    "user_id": 1,
    "username": "john_doe",
    "total_projects": 2,
    "projects": [
        {
            "id": 1,
            "name": "Portfolio Website",
            "description": "My personal portfolio built with Django",
            "tech_stack": [
                {
                    "id": 1,
                    "name": "Django",
                    "logo_url": "https://...",
                    "color": "#092e20"
                }
            ],
            "github_link": "https://github.com/johndoe/portfolio",
            "live_link": "https://johndoe.com",
            "created_at": "2024-01-15T10:30:00Z",
            "updated_at": "2024-01-20T14:20:00Z"
        }
    ]
}
```

### 2. Health Check

**Endpoint:** `GET /api/health/`

**Authentication:** Not required

**Response:**
```json
{
    "status": "API is running",
    "version": "1.0",
    "message": "Portfolio Hub API is active"
}
```

---

## Examples

### cURL Examples

#### Get Projects
```bash
curl -X GET "http://localhost:8000/api/user/1/projects/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

#### Health Check
```bash
curl -X GET "http://localhost:8000/api/health/"
```

### Python Example

```python
import requests

# Your token and user ID
TOKEN = "YOUR_TOKEN_HERE"
USER_ID = 1
BASE_URL = "http://localhost:8000"

# Headers with authentication
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# Get projects
response = requests.get(
    f"{BASE_URL}/api/user/{USER_ID}/projects/",
    headers=headers
)

if response.status_code == 200:
    data = response.json()
    print(f"Found {data['total_projects']} projects")
    
    for project in data['projects']:
        print(f"\nProject: {project['name']}")
        print(f"Description: {project['description']}")
        print(f"Tech Stack: {', '.join([t['name'] for t in project['tech_stack']])}")
        if project['github_link']:
            print(f"GitHub: {project['github_link']}")
        if project['live_link']:
            print(f"Live: {project['live_link']}")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
```

### JavaScript/Fetch Example

```javascript
const TOKEN = "YOUR_TOKEN_HERE";
const USER_ID = 1;
const BASE_URL = "http://localhost:8000";

async function getProjects() {
    try {
        const response = await fetch(
            `${BASE_URL}/api/user/${USER_ID}/projects/`,
            {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${TOKEN}`,
                    'Content-Type': 'application/json'
                }
            }
        );

        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }

        const data = await response.json();
        console.log(`Total Projects: ${data.total_projects}`);
        
        data.projects.forEach(project => {
            console.log(`\n${project.name}`);
            console.log(`${project.description}`);
            console.log(`Tech: ${project.tech_stack.map(t => t.name).join(', ')}`);
        });

        return data;
    } catch (error) {
        console.error('Error fetching projects:', error);
    }
}

getProjects();
```

### JavaScript/Axios Example

```javascript
const axios = require('axios');

const api = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
        'Authorization': 'Bearer YOUR_TOKEN_HERE'
    }
});

api.get('/api/user/1/projects/')
    .then(response => {
        console.log('Projects:', response.data.projects);
    })
    .catch(error => {
        console.error('Error:', error.response.data);
    });
```

### Node.js Example (using node-fetch)

```javascript
const fetch = require('node-fetch');

async function getProjects() {
    const TOKEN = "YOUR_TOKEN_HERE";
    const USER_ID = 1;
    
    const response = await fetch(
        `http://localhost:8000/api/user/${USER_ID}/projects/`,
        {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${TOKEN}`,
                'Content-Type': 'application/json'
            }
        }
    );
    
    const data = await response.json();
    console.log(data);
}

getProjects();
```

### React Example

```javascript
import { useEffect, useState } from 'react';

function ProjectsList() {
    const [projects, setProjects] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const TOKEN = "YOUR_TOKEN_HERE";
        const USER_ID = 1;

        fetch(`http://localhost:8000/api/user/${USER_ID}/projects/`, {
            headers: {
                'Authorization': `Bearer ${TOKEN}`
            }
        })
            .then(res => res.json())
            .then(data => {
                setProjects(data.projects);
                setLoading(false);
            })
            .catch(err => {
                setError(err.message);
                setLoading(false);
            });
    }, []);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;

    return (
        <div>
            {projects.map(project => (
                <div key={project.id}>
                    <h3>{project.name}</h3>
                    <p>{project.description}</p>
                </div>
            ))}
        </div>
    );
}

export default ProjectsList;
```

---

## Error Handling

### Common Error Responses

#### 401 Unauthorized
```json
{
    "error": "Invalid authentication token"
}
```
**Solution:** Check your token is valid and hasn't been regenerated.

#### 403 Forbidden
```json
{
    "error": "You do not have permission to access this resource"
}
```
**Solution:** You can only access your own projects.

#### 404 Not Found
```json
{
    "error": "User not found"
}
```
**Solution:** Check your user ID is correct.

#### 500 Server Error
```json
{
    "error": "Internal server error"
}
```
**Solution:** Check server logs or contact support.

---

## Security Best Practices

1. **Never hardcode tokens** - Use environment variables
   ```bash
   export API_TOKEN="your_token_here"
   ```

2. **Regenerate if compromised** - Go to dashboard and regenerate
3. **Use HTTPS in production** - Change `http://` to `https://`
4. **Keep tokens private** - Don't commit to version control
5. **Use .env files** - Store sensitive data in `.env` file

### Example .env usage (Python)
```python
from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv('API_TOKEN')
```

### Example .env usage (Node.js)
```javascript
require('dotenv').config();
const TOKEN = process.env.API_TOKEN;
```

---

## Rate Limiting

Currently, **no rate limiting** is enforced, but this may change in production.

---

## Troubleshooting

### "Invalid token"
- Token may have been regenerated
- Check you're using the latest token
- Re-generate a new token

### "User not found"
- Check your user ID is correct
- User ID should match your account

### "Permission denied"
- You can only access your own projects
- User ID in URL must match authenticated user

### CORS Issues
- Make sure you're requesting from allowed origins
- In development: `localhost:3000`, `localhost:8000`
- In production: configure ALLOWED_ORIGINS in settings.py

---

## API Response Format

All successful responses follow this format:

```json
{
    "status": "success",
    "data": { /* ... */ }
}
```

All error responses:

```json
{
    "error": "Error message here"
}
```

---

## Testing Your API

### Using Postman

1. Open Postman
2. Create new request
3. Set method to `GET`
4. URL: `http://localhost:8000/api/user/1/projects/`
5. Go to Headers tab
6. Add header: `Authorization: Bearer YOUR_TOKEN`
7. Click Send

### Using Insomnia

1. Open Insomnia
2. Create new request (GET)
3. URL: `http://localhost:8000/api/user/1/projects/`
4. Click Auth dropdown
5. Select "Bearer Token"
6. Paste your token
7. Send

---

## Need Help?

- Check the Django documentation: https://docs.djangoproject.com/
- Check DRF docs: https://www.django-rest-framework.org/
- View our SETUP_INSTRUCTIONS.md for more info

Happy coding! 🚀
