from django.urls import path
from . import views

urlpatterns = [

    path('', views.MainFunctionView.as_view(), name='main'),

    # HOME
    path('home/', views.HomeView.as_view(), name='home'),
    path('update-settings/', views.UpdateSettingsView.as_view(), name='update_settings'),
    path('update-home/', views.UpdateHomeView.as_view(), name='update_home'),
    path('home/add/', views.AddHomeView.as_view(), name='add_home'),
    path('home/edit/<int:pk>/', views.EditHomeView.as_view(), name='edit_home'),
    path('home/delete/<int:pk>/', views.DeleteHomeView.as_view(), name='delete_home'),

    # ABOUT
    path("about/", views.AboutView.as_view(), name="about"),
    path('about/create/', views.CreateAboutView.as_view(), name='create_about'),
    path('about/edit/<int:pk>/', views.EditAboutView.as_view(), name='edit_about'),
    path('about/delete/<int:pk>/', views.DeleteAboutView.as_view(), name='delete_about'),
    path('about/stat/add/', views.AddStatView.as_view(), name='add_stat'),
    path('about/stat/edit/<int:pk>/', views.EditStatView.as_view(), name='edit_stat'),
    path('about/stat/delete/<int:pk>/', views.DeleteStatView.as_view(), name='delete_stat'),

    # SKILLS
    path('skills/', views.SkillListView.as_view(), name='skills'),
    path('skills/add/', views.SkillCreateView.as_view(), name='skill_add'),
    path('skills/edit/<int:pk>/', views.SkillUpdateView.as_view(), name='skill_edit'),
    path('skills/delete/<int:pk>/', views.SkillDeleteView.as_view(), name='skill_delete'),

    path("project/", views.Project.as_view(), name="project"),
    path("timeline/", views.Timeline.as_view(), name="timeline"),

    # ========================================
    # CONTACT SYSTEM - NO /admin/ PREFIX
    # ========================================
    
    # Dashboard
    path('contact/', views.ContactDashboardView.as_view(), name='contact_dashboard'),
    
    # Contact Info
    path('contact/edit/', views.ContactInfoUpdateView.as_view(), name='contact_info_edit'),
    
    # Social Links (NO 'admin/' prefix)
    path('contact/social-links/add/', views.SocialLinkCreateView.as_view(), name='social_link_add'),
    path('contact/social-links/edit/<int:pk>/', views.SocialLinkUpdateView.as_view(), name='social_link_edit'),
    path('contact/social-links/delete/<int:pk>/', views.SocialLinkDeleteView.as_view(), name='social_link_delete'),
    
    # Messages (NO 'admin/' prefix)
    path('contact/messages/detail/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('contact/messages/update-status/<int:pk>/', views.UpdateMessageStatusView.as_view(), name='message_update_status'),
    path('contact/messages/mark-multiple/', views.MarkMultipleMessagesView.as_view(), name='mark_multiple_messages'),
    path('contact/messages/delete/<int:pk>/', views.DeleteMessageView.as_view(), name='message_delete'),
]