from django.shortcuts import render

def home(request):
    return render(request, "blog/home.html")

def posts(request):
    return render(request, "blog/posts.html")

def login_stub(request):
    return render(request, "blog/login_stub.html")

def register_stub(request):
    return render(request, "blog/register_stub.html")
