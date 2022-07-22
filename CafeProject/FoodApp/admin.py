from django.contrib import admin
from . models import Food


class FoodAdim(admin.ModelAdmin):
    list_display = ('f_category', 'f_name', 'f_price', 'f_is_available')


admin.site.register(Food, FoodAdim)
