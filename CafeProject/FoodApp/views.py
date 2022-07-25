from django.shortcuts import render
from . models import Food
from MyApps.models import FoodCategory


# Menu Page
def MenuPage(request):
    food_category = FoodCategory.objects.all()
    foodmenu = Food.objects.all()
    context = {'foodmenu': foodmenu, 'food_category': food_category}
    return render(request, 'food/menu.html', context)


# Details Page
def DetalisPage(request, id):
    foods = Food.objects.get(id=id)
    context = {
        'foods': foods
    }
    return render(request, 'food/details.html', context)
