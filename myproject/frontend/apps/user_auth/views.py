from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages



# ====================================
# ✅ Main Admin Panel (Landing Page)
# ====================================
class Login(View):
    def get(self, request):
        return render(request, 'user_auth/index.html')




