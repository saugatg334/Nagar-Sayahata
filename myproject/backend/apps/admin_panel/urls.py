from django.urls import path
from . import views

app_name = 'admin_panel'  # ✅ NAMESPACE - Make sure this exists!

urlpatterns = [
    # Main dashboard/panel (root path)
    path('', views.MainFunctionView.as_view(), name='main'),
    
    # HOME PAGE
    path('home/', views.Home.as_view(), name='home'),
]