# Social Media API — Task 0: Project Setup & User Authentication

## Overview
This project initializes a Social Media API using Django and Django REST Framework (DRF).  
A custom user model and token-based authentication system were implemented to provide secure API access and support future social features.

---

## Project Setup

### Project Initialization
- Django project created: `social_media_api`
- App created: `accounts`
- Installed apps added:
  - `rest_framework`
  - `rest_framework.authtoken`
  - `accounts`

### Custom User Configuration
A custom user model extending Django’s `AbstractUser` is used.

Additional fields:
- `bio`
- `profile_picture`
- `followers` (ManyToMany self-relationship)

The model is registered in settings using: