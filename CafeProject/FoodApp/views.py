from django.shortcuts import render
from . models import Food
from MyApps.models import FoodCategory


# Menu Page
def MenuPage(request):
    food_category = FoodCategory.objects.all()
    foodmenu = Food.objects.all()
    context = {'foodmenu': foodmenu, 'food_category': food_category}
    return render(request, 'food/menu.html', context)
