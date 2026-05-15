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
        return render(request, 'core/index.html')



