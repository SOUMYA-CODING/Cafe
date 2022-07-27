from django.shortcuts import render
from requests import request


# Index Page
def Index(request):
    return render(request, 'basicpages/index.html')


# About Page
def About(request):
    return render(request, 'basicpages/about.html')


# Contact Page
def Contact(request):
    return render(request, 'basicpages/contact.html')
