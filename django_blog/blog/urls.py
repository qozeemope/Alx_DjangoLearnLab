from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.posts, name="posts"),

    # Temporary stubs (will be replaced in Task 1)
    path("login/", views.login_stub, name="login"),
    path("register/", views.register_stub, name="register"),
]
