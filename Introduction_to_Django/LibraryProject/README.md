# Django Getting Started

Objectives
- Set up a Django development environment.
- Create and run a new Django project.
- Implement and interact with Django models (CRUD via shell).
- Register and customize models in the Django admin.
- Build a foundation for more complex Django apps.

Quick start
1. Create environment and install Django
    $ python -m venv .venv
    $ source .venv/bin/activate   # or .venv\Scripts\activate on Windows
    $ pip install django

2. Create and run project
    $ django-admin startproject myproject .
    $ python manage.py migrate
    $ python manage.py runserver

Create app and models
1. Create app
    $ python manage.py startapp myapp

2. Define models (example in myapp/models.py)
    - Create model classes with fields, e.g. Title, description, timestamps.

3. Apply migrations
    $ python manage.py makemigrations
    $ python manage.py migrate

CRUD with Django shell
$ python manage.py shell
>>> from myapp.models import Item
>>> item = Item.objects.create(name="Example", description="...")
>>> Item.objects.get(pk=item.pk)
>>> item.description = "Updated"
>>> item.save()
>>> item.delete()

Admin interface
1. Register models in myapp/admin.py:
    - from django.contrib import admin
      from .models import Item
      admin.site.register(Item)

2. Customize admin (list_display, search_fields, list_filter) to improve visibility.

Notes
- Keep models small and migrate often.
- Use virtual environments and version control.
- This README is a concise starting guide; expand each step while building the app.