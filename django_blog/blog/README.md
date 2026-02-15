## Django Blog Application

### Overview
This project is a fully functional Django blog application that supports authentication, post management, commenting, tagging, and search.  
It demonstrates how to build a real-world Django web application using models, forms, class-based views, and templates.

---

### Setup Instructions

1. Clone the repository and navigate into the project folder  
2. Install dependencies  
```
pip install django django-taggit
```
3. Run migrations  
```
python manage.py makemigrations
python manage.py migrate
```
4. Start the development server  
```
python manage.py runserver
```
5. Open in browser:  
```
http://127.0.0.1:8000/
```

---

### Project Structure

```
django_blog/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/blog/
│   └── migrations/
│
├── django_blog/
│   ├── settings.py
│   └── urls.py
```

---

### Authentication Features
- User registration with email support  
- Login and logout using Django authentication views  
- Profile page for updating user email  
- Protected routes for authenticated users  

---

### Blog Post Management
- Users can create new posts  
- All visitors can view posts  
- Authors can update or delete only their own posts  
- Posts are ordered by publication date  
- Redirect handled using `get_absolute_url()`

---

### Comment System
- Authenticated users can add comments to posts  
- Comments appear on the post detail page  
- Only the comment author can edit or delete their comment  
- Each comment is linked to both the post and user  

---

### Tagging System
- Posts can include multiple tags  
- Tags are managed using **django-taggit**  
- Tags appear on post list and detail pages  
- Clicking a tag shows all posts with that tag  

---

### Search Feature
Users can search posts using the search bar.

The search checks:
- Post titles  
- Post content  
- Tag names  

Results are displayed on a search results page.

---

### Security
The application uses Django’s built-in protections:

- CSRF protection on all forms  
- Secure password hashing  
- LoginRequiredMixin for protected views  
- Ownership checks for post/comment editing  

---

### Testing Features
To test the application:

1. Register a new account  
2. Login and create a post  
3. Edit or delete your post  
4. Add comments to a post  
5. Click a tag to filter posts  
6. Use the search bar to find content  
