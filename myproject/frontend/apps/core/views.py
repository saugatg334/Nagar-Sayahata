from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages



# ====================================
# ✅ Main Admin Panel (Landing Page)
# ====================================
class Core(View):
    def get(self, request):
        return render(request, 'user_auth/dashboard.html')


#  ====================================
# ✅ Main user (Landing Page)
# ====================================
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

    return render(request, "login.html")

