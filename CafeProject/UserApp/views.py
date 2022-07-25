from django.shortcuts import render


def userLogin(request):
    return render(request, 'authentications/login.html')
