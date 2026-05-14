from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Profile


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
# ✅ Profile Section
# ====================================
class profile(View):
    template_name = 'profile/index.html'

    def get(self, request):
        # Get or create profile for current user
        profile, created = Profile.objects.get_or_create(user=request.user)

        context = {
            'user': request.user,
            'profile': profile,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        # Get or create profile
        profile, created = Profile.objects.get_or_create(user=request.user)

        # Update profile fields
        profile.phone = request.POST.get('phone', '')
        profile.country = request.POST.get('country', '')
        profile.province = request.POST.get('province', '')
        profile.district = request.POST.get('district', '')
        profile.municipality = request.POST.get('municipality', '')
        profile.ward = request.POST.get('ward', '')

        # Handle photo upload
        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']

        profile.save()

        # Update user's name if changed
        new_name = request.POST.get('name', '')
        if new_name:
            request.user.first_name = ' '.join(new_name.split()[:-1])
            request.user.last_name = new_name.split()[-1] if len(new_name.split()) > 1 else ''
            request.user.save()

        messages.success(request, 'Profile saved successfully!')
        return redirect('admin_panel:main')