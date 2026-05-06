from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator

from backend_setup.all_db_connection.models import db_home, DashboardSettings, About, AboutStat, Skill, ContactInfo, SocialLink, Message


# ====================================
# ✅ Main Admin pannel
# ====================================
class MainFunctionView(View):
    def get(self, request):
        return render(request, 'admin_base.html')


# ====================================
# ✅ Home Section ALl
# ====================================
# class Home(View):
#     def get(self, request):
#         # try to get data (safe way)
#         home_data = db_home.objects.first()

#         context = {
#             "home": home_data
#         }

#         return render(request, "all_section/home/home.html", context)



class HomeView(LoginRequiredMixin, View):
    """View to display home dashboard with all data"""
    login_url = 'login'
    
    def get(self, request):
        # Get home data
        home_data = db_home.objects.first()
        
        # Get dashboard settings (create if doesn't exist)
        settings, created = DashboardSettings.objects.get_or_create(
            defaults={
                'featured_projects_count': 6,
                'skills_count': 12,
                'show_projects': True,
                'show_skills': True,
                'show_experience': True
            }
        )
        
        context = {
            'home': home_data,
            'settings': settings,
        }
        return render(request, 'all_section/home/home.html', context)


class UpdateSettingsView(LoginRequiredMixin, View):
    """View to update dashboard settings via popup"""
    login_url = 'login'
    
    def post(self, request):
        try:
            # Get or create settings
            settings, created = DashboardSettings.objects.get_or_create(id=1)
            
            # Update settings from modal form
            settings.featured_projects_count = int(request.POST.get('featured_projects_count', 0))
            settings.skills_count = int(request.POST.get('skills_count', 0))
            settings.show_projects = request.POST.get('show_projects') == 'on'
            settings.show_skills = request.POST.get('show_skills') == 'on'
            settings.show_experience = request.POST.get('show_experience') == 'on'
            settings.save()
            
            # Update home data if provided
            home_data = db_home.objects.first()
            if home_data:
                if request.POST.get('hero_title'):
                    home_data.hero_title = request.POST.get('hero_title')
                if request.POST.get('hero_subtitle'):
                    home_data.hero_subtitle = request.POST.get('hero_subtitle')
                if request.POST.get('resume_link'):
                    home_data.resume_link = request.POST.get('resume_link')
                home_data.save()
            
            messages.success(request, "Settings updated successfully!")
            
        except Exception as e:
            messages.error(request, f"Error updating settings: {str(e)}")
        
        return redirect('home')


class UpdateHomeView(LoginRequiredMixin, View):
    """View to update home section data"""
    login_url = 'login'
    
    def post(self, request):
        try:
            home_data = db_home.objects.first()
            
            if not home_data:
                # Create new if doesn't exist
                home_data = db_home()
            
            # Update home data
            home_data.hero_title = request.POST.get('hero_title')
            home_data.hero_subtitle = request.POST.get('hero_subtitle')
            home_data.resume_link = request.POST.get('resume_link')
            
            if request.FILES.get('hero_image'):
                home_data.hero_image = request.FILES.get('hero_image')
            
            home_data.save()
            messages.success(request, "Home data updated successfully!")
            
        except Exception as e:
            messages.error(request, f"Error updating home data: {str(e)}")
        
        return redirect('home')


# Keep your existing AddHomeView, EditHomeView, DeleteHomeView as they are

class AddHomeView(LoginRequiredMixin, View):
    """View to add new home section data"""
    login_url = 'login'
    
    def get(self, request):
        return render(request, 'all_section/home/add_home.html')
    
    def post(self, request):
        try:
            # Check if data already exists
            if db_home.objects.exists():
                messages.error(request, "Home section data already exists! Please edit existing data.")
                return redirect('home')
            
            # Get form data
            user_id = request.POST.get('user_id')
            hero_title = request.POST.get('hero_title')
            hero_subtitle = request.POST.get('hero_subtitle')
            hero_image = request.FILES.get('hero_image')
            resume_link = request.POST.get('resume_link')
            featured_projects_count = request.POST.get('featured_projects_count', 0)
            skills_count = request.POST.get('skills_count', 0)
            show_projects = request.POST.get('show_projects') == 'on'
            show_skills = request.POST.get('show_skills') == 'on'
            show_experience = request.POST.get('show_experience') == 'on'
            
            # Validation
            if not user_id or not hero_title:
                messages.error(request, "User ID and Hero Title are required!")
                return redirect('add_home')
            
            # Create new record
            home_data = db_home(
                user_id=user_id,
                hero_title=hero_title,
                hero_subtitle=hero_subtitle,
                hero_image=hero_image,
                resume_link=resume_link,
                featured_projects_count=int(featured_projects_count),
                skills_count=int(skills_count),
                show_projects=show_projects,
                show_skills=show_skills,
                show_experience=show_experience
            )
            home_data.save()
            
            messages.success(request, "Home section data added successfully!")
            return redirect('home')
            
        except Exception as e:
            messages.error(request, f"Error adding data: {str(e)}")
            return redirect('add_home')


class EditHomeView(LoginRequiredMixin, View):
    """View to edit home section data"""
    login_url = 'login'
    
    def get(self, request, pk):
        home_data = get_object_or_404(db_home, pk=pk)
        context = {
            'home': home_data,
        }
        return render(request, 'all_section/home/edit_home.html', context)
    
    def post(self, request, pk):
        try:
            home_data = get_object_or_404(db_home, pk=pk)
            
            # Get form data
            home_data.user_id = request.POST.get('user_id')
            home_data.hero_title = request.POST.get('hero_title')
            home_data.hero_subtitle = request.POST.get('hero_subtitle')
            
            # Handle image upload
            if request.FILES.get('hero_image'):
                home_data.hero_image = request.FILES.get('hero_image')
            
            home_data.resume_link = request.POST.get('resume_link')
            home_data.featured_projects_count = int(request.POST.get('featured_projects_count', 0))
            home_data.skills_count = int(request.POST.get('skills_count', 0))
            home_data.show_projects = request.POST.get('show_projects') == 'on'
            home_data.show_skills = request.POST.get('show_skills') == 'on'
            home_data.show_experience = request.POST.get('show_experience') == 'on'
            
            # Validation
            if not home_data.user_id or not home_data.hero_title:
                messages.error(request, "User ID and Hero Title are required!")
                return redirect('edit_home', pk=pk)
            
            home_data.save()
            
            messages.success(request, "Home section data updated successfully!")
            return redirect('home')
            
        except Exception as e:
            messages.error(request, f"Error updating data: {str(e)}")
            return redirect('edit_home', pk=pk)


class DeleteHomeView(LoginRequiredMixin, View):
    """View to delete home section data"""
    login_url = 'login'
    
    def post(self, request, pk):
        try:
            home_data = get_object_or_404(db_home, pk=pk)
            home_data.delete()
            messages.success(request, "Home section data deleted successfully!")
        except Exception as e:
            messages.error(request, f"Error deleting data: {str(e)}")
        
        return redirect('home')
    


# ====================================
# ✅ About Section ALl
# ====================================
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class AboutView(LoginRequiredMixin, View):
    """Display About section with all stats"""
    login_url = 'login'
    
    def get(self, request):
        about = About.objects.first()
        stats = AboutStat.objects.all()
        
        context = {
            'about': about,
            'stats': stats,
            'has_about': about is not None,
        }
        return render(request, 'all_section/about/about.html', context)


class CreateAboutView(LoginRequiredMixin, View):
    """Create new About section"""
    login_url = 'login'
    
    def get(self, request):
        if About.objects.exists():
            messages.warning(request, "About section already exists! You can edit it instead.")
            return redirect('about')
        return render(request, 'all_section/about/about_form.html', {'is_edit': False})
    
    def post(self, request):
        if About.objects.exists():
            messages.error(request, "About section already exists!")
            return redirect('about')
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if not title or not description:
            messages.error(request, "Title and description are required!")
            return redirect('create_about')
        
        about = About.objects.create(title=title, description=description)
        messages.success(request, "About section created successfully!")
        return redirect('about')


class EditAboutView(LoginRequiredMixin, View):
    """Edit existing About section"""
    login_url = 'login'
    
    def get(self, request, pk):
        about = get_object_or_404(About, pk=pk)
        return render(request, 'all_section/about/about_form.html', {'about': about, 'is_edit': True})
    
    def post(self, request, pk):
        about = get_object_or_404(About, pk=pk)
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if not title or not description:
            messages.error(request, "Title and description are required!")
            return redirect('edit_about', pk=pk)
        
        about.title = title
        about.description = description
        about.save()
        
        messages.success(request, "About section updated successfully!")
        return redirect('about')


class DeleteAboutView(LoginRequiredMixin, View):
    """Delete About section"""
    login_url = 'login'
    
    def post(self, request, pk):
        about = get_object_or_404(About, pk=pk)
        about.delete()
        messages.success(request, "About section deleted successfully!")
        return redirect('about')


class AddStatView(LoginRequiredMixin, View):
    """Add new stat"""
    login_url = 'login'
    
    def post(self, request):
        value = request.POST.get('value')
        label = request.POST.get('label')
        
        if not value or not label:
            messages.error(request, "Both value and label are required!")
            return redirect('about')
        
        AboutStat.objects.create(value=value, label=label)
        messages.success(request, "Stat added successfully!")
        return redirect('about')


class EditStatView(LoginRequiredMixin, View):
    """Edit existing stat"""
    login_url = 'login'
    
    def post(self, request, pk):
        stat = get_object_or_404(AboutStat, pk=pk)
        
        value = request.POST.get('value')
        label = request.POST.get('label')
        
        if not value or not label:
            messages.error(request, "Both value and label are required!")
            return redirect('about')
        
        stat.value = value
        stat.label = label
        stat.save()
        
        messages.success(request, "Stat updated successfully!")
        return redirect('about')


class DeleteStatView(LoginRequiredMixin, View):
    """Delete stat"""
    login_url = 'login'
    
    def post(self, request, pk):
        stat = get_object_or_404(AboutStat, pk=pk)
        stat.delete()
        messages.success(request, "Stat deleted successfully!")
        return redirect('about')


# ====================================
# ✅ Skills Section ALl
# ====================================
# class Skills(View):
#     def get(self, request):
#         return render(request, "all_section/skills/skills.html")
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import models

class SkillListView(LoginRequiredMixin, ListView):
    """Display all skills in a grid layout"""
    model = Skill
    template_name = 'all_section/skills/skills_list.html'
    context_object_name = 'skills'
    login_url = 'login'
    
    def get_queryset(self):
        return Skill.objects.all().order_by('-percentage', 'skill_name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_skills'] = self.get_queryset().count()
        context['avg_percentage'] = self.get_queryset().aggregate(
            avg=models.Avg('percentage')
        )['avg'] or 0
        return context


class SkillCreateView(LoginRequiredMixin, CreateView):
    """Add new skill"""
    model = Skill
    fields = ['skill_name', 'percentage']
    template_name = 'all_section/skills/skill_form.html'
    login_url = 'login'
    success_url = reverse_lazy('skills')
    
    def form_valid(self, form):
        messages.success(self.request, f'Skill "{form.instance.skill_name}" added successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    """Edit existing skill"""
    model = Skill
    fields = ['skill_name', 'percentage']
    template_name = 'all_section/skills/skill_form.html'
    login_url = 'login'
    success_url = reverse_lazy('skills')
    
    def form_valid(self, form):
        messages.success(self.request, f'Skill "{form.instance.skill_name}" updated successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    """Delete skill"""
    model = Skill
    template_name = 'all_section/skills/skill_confirm_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('skills')
    
    def delete(self, request, *args, **kwargs):
        skill = self.get_object()
        skill_name = skill.skill_name
        messages.success(request, f'Skill "{skill_name}" deleted successfully!')
        return super().delete(request, *args, **kwargs)


# ====================================
# ✅ Project Section ALl
# ====================================
class Project(View):
    def get(self, request):
        return render(request, "all_section/project/project.html")


# ====================================
# ✅ Timeline Section ALl
# ====================================
class Timeline(View):
    def get(self, request):
        return render(request, "all_section/timeline/timeline.html")


# ====================================
# ✅ Contact Section ALl
# ====================================
class ContactDashboardView(LoginRequiredMixin, TemplateView):
    """Single page dashboard for contact management"""
    login_url = 'login'
    template_name = 'all_section/contact/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Contact Info
        context['contact_info'] = ContactInfo.objects.first()
        
        # Social Links
        context['social_links'] = SocialLink.objects.all().order_by('platform')
        
        # Messages with filtering
        queryset = Message.objects.all().order_by('-created_at')
        status_filter = self.request.GET.get('status')
        
        if status_filter and status_filter != 'all':
            queryset = queryset.filter(status=status_filter)
        
        # Pagination
        paginator = Paginator(queryset, 10)
        page = self.request.GET.get('page', 1)
        messages_page = paginator.get_page(page)
        
        context['messages'] = messages_page
        context['unread_count'] = Message.objects.filter(status='unread').count()
        context['read_count'] = Message.objects.filter(status='read').count()
        context['replied_count'] = Message.objects.filter(status='replied').count()
        context['total_count'] = Message.objects.count()
        context['current_filter'] = status_filter or 'all'
        
        return context


class ContactInfoUpdateView(LoginRequiredMixin, View):
    """Update contact information via AJAX"""
    login_url = 'login'
    
    def post(self, request):
        contact_info = ContactInfo.objects.first()
        if not contact_info:
            contact_info = ContactInfo()
        
        contact_info.email = request.POST.get('email')
        contact_info.phone = request.POST.get('phone')
        contact_info.location = request.POST.get('location')
        contact_info.description = request.POST.get('description')
        contact_info.save()
        
        return JsonResponse({'status': 'success'})


class SocialLinkCreateView(LoginRequiredMixin, View):
    """Add new social link via AJAX"""
    login_url = 'login'
    
    def post(self, request):
        platform = request.POST.get('platform')
        url = request.POST.get('url')
        
        icon_map = {
            'github': 'fab fa-github', 'linkedin': 'fab fa-linkedin-in',
            'twitter': 'fab fa-twitter', 'facebook': 'fab fa-facebook-f',
            'instagram': 'fab fa-instagram', 'youtube': 'fab fa-youtube',
            'dribbble': 'fab fa-dribbble', 'behance': 'fab fa-behance',
            'medium': 'fab fa-medium-m', 'stackoverflow': 'fab fa-stack-overflow',
            'discord': 'fab fa-discord', 'telegram': 'fab fa-telegram',
            'whatsapp': 'fab fa-whatsapp', 'other': 'fas fa-link',
        }
        
        SocialLink.objects.create(
            platform=platform,
            url=url,
            icon_class=icon_map.get(platform, 'fas fa-link')
        )
        
        return JsonResponse({'status': 'success'})


class SocialLinkUpdateView(LoginRequiredMixin, View):
    """Update social link via AJAX"""
    login_url = 'login'
    
    def post(self, request, pk):
        link = get_object_or_404(SocialLink, pk=pk)
        link.platform = request.POST.get('platform')
        link.url = request.POST.get('url')
        
        icon_map = {
            'github': 'fab fa-github', 'linkedin': 'fab fa-linkedin-in',
            'twitter': 'fab fa-twitter', 'facebook': 'fab fa-facebook-f',
            'instagram': 'fab fa-instagram', 'youtube': 'fab fa-youtube',
            'dribbble': 'fab fa-dribbble', 'behance': 'fab fa-behance',
            'medium': 'fab fa-medium-m', 'stackoverflow': 'fab fa-stack-overflow',
            'discord': 'fab fa-discord', 'telegram': 'fab fa-telegram',
            'whatsapp': 'fab fa-whatsapp', 'other': 'fas fa-link',
        }
        link.icon_class = icon_map.get(link.platform, 'fas fa-link')
        link.save()
        
        return JsonResponse({'status': 'success'})


class SocialLinkDeleteView(LoginRequiredMixin, View):
    """Delete social link via AJAX"""
    login_url = 'login'
    
    def post(self, request, pk):
        link = get_object_or_404(SocialLink, pk=pk)
        link.delete()
        return JsonResponse({'status': 'success'})


class MessageDetailView(LoginRequiredMixin, View):
    """Get message details for modal"""
    login_url = 'login'
    
    def get(self, request, pk):
        message = get_object_or_404(Message, pk=pk)
        return JsonResponse({
            'id': message.id,
            'name': message.name,
            'email': message.email,
            'subject': message.get_subject_display(),
            'message': message.message,
            'status': message.status,
            'created_at': message.created_at.strftime("%B %d, %Y %I:%M %p"),
        })


class UpdateMessageStatusView(LoginRequiredMixin, View):
    """Update message status via AJAX"""
    login_url = 'login'
    
    def post(self, request, pk):
        message = get_object_or_404(Message, pk=pk)
        new_status = request.POST.get('status')
        
        if new_status in ['read', 'replied']:
            message.status = new_status
            message.save()
        
        return JsonResponse({'status': 'success'})


class MarkMultipleMessagesView(LoginRequiredMixin, View):
    """Mark multiple messages"""
    login_url = 'login'
    
    def post(self, request):
        message_ids = request.POST.getlist('message_ids')
        action = request.POST.get('action')
        
        if not message_ids:
            return JsonResponse({'status': 'error'}, status=400)
        
        if len(message_ids) == 1 and ',' in message_ids[0]:
            message_ids = message_ids[0].split(',')
        
        if action == 'read':
            Message.objects.filter(id__in=message_ids).update(status='read')
        elif action == 'replied':
            Message.objects.filter(id__in=message_ids).update(status='replied')
        elif action == 'delete':
            Message.objects.filter(id__in=message_ids).delete()
        
        return JsonResponse({'status': 'success'})


class DeleteMessageView(LoginRequiredMixin, View):
    """Delete single message"""
    login_url = 'login'
    
    def post(self, request, pk):
        message = get_object_or_404(Message, pk=pk)
        message.delete()
        return JsonResponse({'status': 'success'})
    



