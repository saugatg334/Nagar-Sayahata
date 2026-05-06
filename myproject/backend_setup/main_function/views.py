from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import JsonResponse


# ====================================
# ✅ Main Admin pannel
# ====================================
class MainFunctionView(View):
    def get(self, request):
        return render(request, 'admin_base.html')


# ====================================
# ✅ Home Section ALl
# ====================================
class Home(LoginRequiredMixin, TemplateView):
    def get(self, request):
        return render(request, "all_section/home/home.html")





