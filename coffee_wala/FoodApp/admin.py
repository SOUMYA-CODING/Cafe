from django.contrib import admin
from . models import Category, FoodItem, Orders

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_details', 'is_ready', 'is_delivered')
    list_editable = ('is_ready', 'is_delivered')
    ordering = ('-id',)

admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(Orders, OrderAdmin)
