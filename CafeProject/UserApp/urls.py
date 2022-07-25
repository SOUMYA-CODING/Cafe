from django.urls import path
from . import views

urlpatterns = [
    path('userlogin/', views.userLogin, name="user_login_page"),
]
