from django.urls import path
from . import views

app_name = 'admin_panel'  # ✅ NAMESPACE - Make sure this exists!

urlpatterns = [
    # Main dashboard
    path('login/', views.Login.as_view(), name='login'),

    
]
