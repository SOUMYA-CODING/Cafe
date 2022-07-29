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


# Search Page
def Search(request):
    return render(request, 'basicpages/search.html')


def SearchBtn(request):
    if request.method == "POST":
        food_name = request.POST.get("searchinput")
        foodItems = FoodItem.objects.filter(food_name=FoodItem.name)

        context = {
            'foodItems': foodItems
        }
    return render(request, 'basicpages/search.html', context)
