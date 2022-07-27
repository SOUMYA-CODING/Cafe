from logging import exception
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Login Page
def Login(request):
    # Error
    error = False

    # Get the data from form
    if request.method == "POST":
        username = request.POST.get('sic_number')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'user/login.html')


# Registartion Page
def Registartion(request):
    # Error
    error = False

    # Get the data from form
    if request.method == "POST":
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        username = request.POST.get('sic_number')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        # Check is SIC Number exits or not
        if User.objects.filter(username=username).exists():
            messages.error(request, "SIC Number already exits")
            error = True

        # Check is Email exits or not
        if User.objects.filter(email=email).exists():
            messages.error(request, "E-mail ID already exits")
            error = True

        # Chech error
        if error:
            return render(request, 'user/registration.html')

        # Create user
        try:
            user = User.objects.create_user(
                first_name=f_name,
                last_name=l_name,
                username=username,
                email=email,
                password=password
            )
            user.save()
            messages.success(
                request, "Account created Successfully. Login to continue")
            return redirect('login')

        except Exception as e:
            messages.error(request, e)

    return render(request, 'user/registration.html')


# Logout
def Logout(request):
    logout(request)
    return redirect('index')
