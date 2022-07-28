from django.urls import path
from . import views


# FoodApp Urls
urlpatterns = [
    path('menu/', views.Menu, name="menu"),
    path('itemDetail/<int:id>/', views.ItemDetails, name="itemDetails"),
    path('add_to_cart/', views.AddCart, name="addtoCart"),
    path('cartDetails/', views.CartDetails, name="cartDetails"),
    path('deleteItem/<str:id>/', views.DeleteCardItem, name="deleteItem"),
    path('checkOut/', views.OtpPage, name="checkOut"),
]
