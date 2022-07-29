from unicodedata import name
from django.shortcuts import render
from FoodApp.models import FoodItem
from django.db.models import Q


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


# Search Page
def Search(request):
    return render(request, 'basicpages/search.html')


def SearchBtn(request):
    if request.method == "GET":
        food_name = request.GET.get("searchinput")
        foods = FoodItem.objects.filter(Q(name__icontains=food_name))
        context = {
            'food': foods,
        }
    return render(request, 'basicpages/search.html', context)
