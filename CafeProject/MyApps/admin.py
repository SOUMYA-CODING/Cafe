from django.contrib import admin
from . models import FoodCategory


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('fc_name', 'fc_craeted_at')


admin.site.register(FoodCategory, FoodCategoryAdmin)
