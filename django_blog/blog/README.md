## Blog Post Management Features

### Overview
The blog application supports full CRUD (Create, Read, Update, Delete) operations for blog posts. These features are implemented using Django’s class-based generic views together with ModelForms to ensure structured validation and secure data handling.

---

### Create Post
Authenticated users can create new blog posts using a form interface.  
The backend automatically assigns the logged-in user as the post author, ensuring that users cannot create posts on behalf of others.

After a successful submission, the system redirects to the post’s detail page using the model’s `get_absolute_url()` method.

---

### Read Posts
All visitors, including anonymous users, can:
- View the list of all blog posts
- Open individual post detail pages

Posts are displayed in reverse chronological order based on their publication date.

---

### Update Post
Only the original author of a post is allowed to edit it.

This restriction is enforced using:
- `LoginRequiredMixin` to ensure the user is authenticated
- `UserPassesTestMixin` t
