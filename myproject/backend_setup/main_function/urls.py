from django.urls import path
from . import views

urlpatterns = [

    path('', views.MainFunctionView.as_view(), name='main'),

    # HOME
    path('home/', views.Home.as_view(), name='home'),
    
    
]