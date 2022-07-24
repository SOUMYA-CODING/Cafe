from django.shortcuts import render
from . models import FoodCategory


# Index Page
def index(request):
    food_category = FoodCategory.objects.all()
    contexts = {
        'food_category': food_category
    }
    return render(request, 'mainpage/index.html', contexts)


# About Us Page
def about(request):
    return render(request, 'mainpage/about.html')


# Contact Page
def contact(request):
    return render(request, 'mainpage/contact.html')


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
