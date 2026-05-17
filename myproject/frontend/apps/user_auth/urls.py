from django.urls import path
from . import views

app_name = 'user_auth'  # ✅ NAMESPACE - Make sure this exists!

urlpatterns = [
    # Main dashboard
    path('login/', views.Login.as_view(), name='login'),

    # Logout
    path('logout/', views.Logout.as_view(), name='logout'),

    # Registration
    path('register/', views.Register.as_view(), name='register'),
    


]
