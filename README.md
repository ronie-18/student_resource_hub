# Student Resource Hub

A comprehensive web application for students to share, discover, and download educational resources. Built with Django, this platform allows users to upload, categorize, and access academic materials in a user-friendly environment.

## Features

- **User Authentication System**
  - Custom user model with profile management
  - Registration, login, and logout functionality
  - Profile customization with bio and profile image

- **Resource Management**
  - Upload educational resources with descriptions and thumbnails
  - Categorize resources for easy discovery
  - Search functionality with filtering by category
  - Download tracking for resources

- **Modern UI/UX**
  - Responsive Bootstrap-based design
  - Intuitive navigation and user interface
  - Mobile-friendly layout

- **Newsletter Subscription**
  - Email subscription system for updates
  - Subscription management

## Technology Stack

- **Backend**: Django 4.2.10
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Authentication**: Django's built-in authentication with custom user model
- **Form Processing**: django-crispy-forms with Bootstrap 5
- **File Handling**: Django's FileField and ImageField
- **API Support**: Django REST Framework

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/student_resource_hub.git
   cd student_resource_hub
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## Project Structure

```
student_resource_hub/
├── media/                  # User-uploaded files
├── resources/              # Resources app
│   ├── migrations/         # Database migrations
│   ├── models.py           # Resource and Category models
│   ├── views.py            # View functions
│   ├── urls.py             # URL routing
│   ├── forms.py            # Forms for resource management
│   └── admin.py            # Admin configuration
├── static/                 # Static files (CSS, JS, images)
├── student_resource_hub/   # Project settings
├── templates/              # HTML templates
│   ├── base/               # Base templates
│   ├── resources/          # Resource-related templates
│   └── users/              # User-related templates
├── users/                  # Users app
│   ├── migrations/         # Database migrations
│   ├── models.py           # CustomUser model
│   ├── views.py            # User-related views
│   ├── urls.py             # URL routing
│   ├── forms.py            # User forms
│   └── admin.py            # Admin configuration
├── manage.py               # Django management script
└── requirements.txt        # Project dependencies
```

## Usage

### For Students

1. Register for an account or log in
2. Browse resources by category or search for specific topics
3. Download resources for your studies
4. Upload your own study materials to share with others
5. Subscribe to the newsletter for updates

### For Administrators

1. Access the admin panel at `/admin`
2. Manage users, resources, and categories
3. Monitor resource uploads and downloads
4. Manage newsletter subscriptions

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please contact: rounakjana04968@gmail.com