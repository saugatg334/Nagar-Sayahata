from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView


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
            'user': request.user,  # Pass user to template
        }
        return render(request, self.template_name, context)





