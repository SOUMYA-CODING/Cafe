from django.shortcuts import render


# Index Page
def index(request):
    return render(request, 'base/index.html')


# Login Page
def login(request):
    return render(request, 'authentications/login.html')


# Registration Page
def registration(request):
    return render(request, 'authentications/registration.html')


# Password Reset Page
def password_reset(request):
    return render(request, 'authentications/password_reset.html')


# Cart Page
def cart(request):
    return render(request, 'operations/cart.html')


# Orders Page
def orders(request):
    return render(request, 'operations/orders.html')
