from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuPage, name="menu_page")
]
