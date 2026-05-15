from django.urls import path
from . import views

app_name = 'core'  # ✅ NAMESPACE - Make sure this exists!

urlpatterns = [
    # Main dashboard
    path('navbar/', views.Core.as_view(), name='main'),

    

]
