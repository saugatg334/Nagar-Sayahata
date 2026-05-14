from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages



# ====================================
# ✅ Main Admin Panel (Landing Page)
# ====================================
class MainFunctionView(View):
    def get(self, request):
        return render(request, 'admin_panel.html')


# ====================================
# ✅ Home Section
# ====================================
class Home(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        context = {
            'user': request.user,
        }
        return render(request, self.template_name, context)


# ====================================
# ✅ About Section
# ====================================
class About(TemplateView):
    template_name = 'about/about.html'

    def get(self, request):
        context = {
            'user': request.user,
        }
        return render(request, self.template_name, context)


# ====================================
# ✅ Profile Section
# ====================================
class profile(View):
    template_name = 'profile/index.html'

    def get(self, request):
        context = {
            'user': request.user,
        }
        return render(request, self.template_name, context)
    
    
