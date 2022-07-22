from django.contrib import admin
from . models import Food


class FoodAdim(admin.ModelAdmin):
    list_display = ('f_category', 'f_name', 'f_price', 'f_is_available')
    list_editable = ('f_is_available',)
    search_fields = ('f_name',)
    list_filter = ('f_is_available',)

admin.site.register(Food, FoodAdim)
