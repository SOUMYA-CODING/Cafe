from django.shortcuts import render
from . models import Food


# Menu Page
def MenuPage(request):
    foodmenu = Food.objects.all()
    context = {'foodmenu': foodmenu}
    return render(request, 'food/menu.html', context)
