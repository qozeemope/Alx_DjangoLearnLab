## Blog Post Management Features

The blog supports full CRUD operations for posts using Django class-based views and ModelForms.

- **Create:** Authenticated users can create posts. The system automatically assigns the logged-in user as the author and redirects to the post detail page after submission.
- **Read:** All users can view the post list and individual post pages. Posts are ordered by newest first.
- **Update:** Only the post author can edit a post. Access is enforced using authentication and ownership checks.
- **Delete:** Only the author can delete their post. Unauthorized users are blocked by backend permission rules.

---

## Comment System

The application includes a comment feature that allows discussion on posts.

- **Create:** Logged-in users can add comments from the post detail page. The backend links each comment to the current user and post automatically.
- **Display:** Comments appear on the post page in chronological order with author and timestamp.
- **Update/Delete:** Only the comment author can edit or remove their comment.
- **Security:** Authentication checks, ownership validation, CSRF protection, and database relationships ensure secure comment handling.

---

## Tagging and Search Features

Tagging and search improve content organization and discoverability.

### Tagging
- Posts can include multiple tags entered as comma-separated values.
- Tags are stored as reusable database objects and linked to posts.
- Clicking a tag shows all posts associated with it.

### Search
- Users can search posts using a keyword.
- The system searches:
  - post titles  
  - post content  
  - tag names  
- Results are displayed on a dedicated search results page.

---

These features enhance usability by allowing users to organize posts, explore related content, and quickly find information.
