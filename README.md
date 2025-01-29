# Public API that retrieves information

This is a simple REST API built with Django REST Framework that provides basic information including an email address, current UTC datetime, and GitHub URL.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone "https://github.com/Kenward-dev"
   cd Kenward-dev
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

### Endpoint
- URL: `GET /`
- No authentication required
- No parameters required

### Response Format
```json
{
    "email": "codewithkenward@gmail.com",
    "current_datetime": "2025-01-28T12:00:00Z",
    "github_url": "https://github.com/Kenward-dev"
}
```

### Example Usage
```bash
curl https://varying-juana-kenward-faf125f0.koyeb.app/
```

## Links
- [HNG Python Developers](https://hng.tech/hire/python-developers)
- [HNG C# Developers](https://hng.tech/hire/csharp-developers)
- [HNG Golang Developers](https://hng.tech/hire/golang-developers)
- [HNG PHP Developers](https://hng.tech/hire/php-developers)
- [HNG Java Developers](https://hng.tech/hire/java-developers)
- [HNG NodeJS Developers](https://hng.tech/hire/nodejs-developers)