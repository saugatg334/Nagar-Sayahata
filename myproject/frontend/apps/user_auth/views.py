from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages


# ====================================
# ✅ Login View
# ====================================
from django.contrib.auth import authenticate, login


# ====================================
# ✅ Login View
# ====================================
class Login(View):

    # show login page
    def get(self, request):

        return render(
            request,
            'user_auth/index.html'
        )

    # handle login form
    def post(self, request):

        username = request.POST.get("username")
        password = request.POST.get("password")

        # check empty fields
        if not username or not password:

            messages.error(
                request,
                "All fields are required."
            )

            return render(
                request,
                'user_auth/index.html'
            )

        # authenticate user
        user = authenticate(
            request,
            username=username,
            password=password
        )

        # valid login
        if user is not None:

            login(request, user)

            messages.success(
                request,
                "Login successful."
            )

            return redirect('dashboard')

        # invalid login
        else:

            messages.error(
                request,
                "Invalid username or password."
            )

            return render(
                request,
                'user_auth/index.html'
            )
# ====================================
# ✅ Logout View
# ====================================
class Logout(View):

    def get(self, request):

        if request.user.is_authenticated:

            logout(request)

            messages.info(
                request,
                "You have been successfully logged out."
            )

        else:

            messages.info(
                request,
                "You were not logged in."
            )

        return redirect('user_auth:login')


# ====================================
# ✅ Register View
# ====================================
class Register(View):

    # show register page
    def get(self, request):

        return render(
            request,
            'user_auth/register.html'
        )

    # handle form submit
    def post(self, request):

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # check empty fields
        if not username or not email or not password:

            messages.error(
                request,
                "All fields are required."
            )

            return render(
                request,
                'user_auth/register.html'
            )

        # check existing username
        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return render(
                request,
                'user_auth/register.html'
            )

        # create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Account created successfully."
        )

        return redirect('user_auth:login')
        from django.http import HttpResponse


def dashboard(request):
    return HttpResponse("Dashboard Working Successfully")