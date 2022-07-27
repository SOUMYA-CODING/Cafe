from django.urls import path
from . import views


# UserApp Urls
urlpatterns = [
    path('login/', views.Login, name="login"),
    path('registartion/', views.Registartion, name="registartion"),
    path('logout/', views.Logout, name="logout")
]
