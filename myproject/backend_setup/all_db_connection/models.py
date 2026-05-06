from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    


class db_home(models.Model):
    user_id = models.CharField(max_length=100, unique=True)

    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.CharField(max_length=300)
    hero_image = models.ImageField(upload_to='all_pictures/images/home/', null=True, blank=True)
    resume_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.hero_title


class DashboardSettings(models.Model):
    user_id = models.CharField(max_length=100, unique=True)

    featured_projects_count = models.PositiveIntegerField(default=0)
    skills_count = models.PositiveIntegerField(default=0)

    show_projects = models.BooleanField(default=True)
    show_skills = models.BooleanField(default=True)
    show_experience = models.BooleanField(default=True)

    def __str__(self):
        return f"Settings for {self.user_id}"



class About(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class AboutStat(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=50)    # e.g. "3+"
    label = models.CharField(max_length=100)   # e.g. "Years Experience"
    

    def __str__(self):
        return f"{self.label} - {self.value}"


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.skill_name} - {self.percentage}%"




# =========================
# CONTACT INFO (about contact page details)
# =========================
class ContactInfo(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Contact Info - {self.email}"
    
    class Meta:
        verbose_name_plural = "Contact Information"


class SocialLink(models.Model):
    id = models.AutoField(primary_key=True)
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('dribbble', 'Dribbble'),
        ('behance', 'Behance'),
        ('medium', 'Medium'),
        ('stackoverflow', 'Stack Overflow'),
        ('discord', 'Discord'),
        ('telegram', 'Telegram'),
        ('whatsapp', 'WhatsApp'),
        ('other', 'Other'),
    ]
    
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(max_length=100, blank=True, help_text="FontAwesome icon class")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_platform_display()} - {self.url}"
    
    class Meta:
        ordering = ['platform']


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    SUBJECT_CHOICES = [
        ('inquiry', 'Inquiry'),
        ('job_offer', 'Job Offer'),
        ('collaboration', 'Collaboration'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('unread', 'Unread'),
        ('read', 'Read'),
        ('replied', 'Replied'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='unread'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.get_status_display()}"
    
    class Meta:
        ordering = ['-created_at']









