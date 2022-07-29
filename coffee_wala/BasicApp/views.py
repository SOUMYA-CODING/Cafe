from django.shortcuts import render
from FoodApp.models import FoodItem


# Index Page
def Index(request):
    foodItems = FoodItem.objects.all()
    context = {
        'foodItems': foodItems,
    }
    return render(request, 'basicpages/index.html', context)


# About Page
def About(request):
    return render(request, 'basicpages/about.html')


# Contact Page
def Contact(request):
    return render(request, 'basicpages/contact.html')
