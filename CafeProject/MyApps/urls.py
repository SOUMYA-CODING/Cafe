from django.urls import path
from . import views

# URLS
urlpatterns = [
    path('', views.index, name="index_page"),
    path('login/', views.login, name="login_page"),
    path('registration/', views.registration, name="registration_page"),
    path('password_reset/', views.password_reset, name="password_reset_page"),
    path('cart/', views.cart, name="cart_page"),
    path('orders/', views.orders, name="orders_page"),
]
