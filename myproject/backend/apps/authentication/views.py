
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.cache import cache
from django.utils.timezone import now
from django.conf import settings
import time


class LoginView(View):
    # Brute force protection settings
    MAX_ATTEMPTS = 5
    LOCKOUT_TIME = 20  # seconds
    
    def get_failed_attempts(self, request):
        """Get failed login attempts for current session/IP"""
        # Use IP address for tracking (more secure than session alone)
        ip_address = self.get_client_ip(request)
        cache_key = f'login_attempts_{ip_address}'
        
        attempts = cache.get(cache_key)
        if attempts is None:
            return {'count': 0, 'timestamp': None}
        return attempts
    
    def get_client_ip(self, request):
        """Get client IP address from request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def is_locked_out(self, request):
        """Check if IP/session is currently locked out"""
        attempts_data = self.get_failed_attempts(request)
        
        if attempts_data['count'] >= self.MAX_ATTEMPTS:
            # Check if lockout period has expired
            if attempts_data['timestamp']:
                lockout_until = attempts_data['timestamp'] + self.LOCKOUT_TIME
                if now().timestamp() < lockout_until:
                    remaining_time = int(lockout_until - now().timestamp())
                    return True, remaining_time
                else:
                    # Lockout expired, reset attempts
                    self.reset_failed_attempts(request)
                    return False, 0
        return False, 0
    
    def record_failed_attempt(self, request):
        """Record a failed login attempt"""
        ip_address = self.get_client_ip(request)
        cache_key = f'login_attempts_{ip_address}'
        
        attempts_data = self.get_failed_attempts(request)
        
        # Update attempts count and timestamp
        attempts_data['count'] += 1
        attempts_data['timestamp'] = now().timestamp()
        
        # Store in cache with expiry (longer than lockout time)
        cache.set(cache_key, attempts_data, timeout=300)  # 5 minutes expiry
    
    def reset_failed_attempts(self, request):
        """Reset failed attempts on successful login"""
        ip_address = self.get_client_ip(request)
        cache_key = f'login_attempts_{ip_address}'
        cache.delete(cache_key)
    
    def add_delay_on_failure(self, request):
        """Add progressive delay on repeated failures to slow down brute force"""
        attempts_data = self.get_failed_attempts(request)
        attempt_count = attempts_data['count']
        
        if attempt_count > 0:
            # Progressive delay: 0.5s, 1s, 2s, 3s, 4s
            delay = min(attempt_count * 0.5, 4)
            time.sleep(delay)
    
    def get(self, request):
        """Render login page"""
        # If user is already logged in, redirect to home
        if request.user.is_authenticated:
            return redirect('admin_pannel:home')
        
        # Check if there's a lockout message to display
        is_locked, remaining = self.is_locked_out(request)
        if is_locked:
            messages.warning(request, f"Too many failed attempts. Please try again after {remaining} seconds.")
        
        return render(request, "authentication/login.html")
    
    def post(self, request):
        """Handle login POST request with brute force protection"""
        
        # Check if already authenticated
        if request.user.is_authenticated:
            return redirect('admin_pannel:home')
        
        # Check for lockout FIRST (before any authentication attempt)
        is_locked, remaining_time = self.is_locked_out(request)
        
        if is_locked:
            messages.error(request, f"Too many failed attempts. Please wait {remaining_time} seconds before trying again.")
            return redirect('auth:login')
        
        # Get credentials
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        # Basic validation
        if not username or not password:
            messages.error(request, "Invalid credentials")
            self.record_failed_attempt(request)
            self.add_delay_on_failure(request)
            return redirect('auth:login')
        
        # Attempt authentication
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            # Successful login - reset attempts and login user
            self.reset_failed_attempts(request)
            login(request, user)
            
            # Clear any existing lockout messages
            # messages.success(request, f"Welcome back, {user.username}!")
            
            # Redirect to next parameter if exists
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            
            return redirect('admin_pannel:home')
        else:
            # Failed login - record attempt and show generic message
            self.record_failed_attempt(request)
            self.add_delay_on_failure(request)
            
            # Generic error message (don't reveal if username or password is wrong)
            messages.error(request, "Invalid credentials")
            
            # Check if this attempt caused lockout
            is_now_locked, remaining = self.is_locked_out(request)
            if is_now_locked:
                messages.warning(request, f"Too many failed attempts. Please try again after {remaining} seconds.")
            
            return redirect('auth:login')


class LogoutView(View):
    def get(self, request):
        """Logout user and clear session"""
        if request.user.is_authenticated:
            username = request.user.username
            logout(request)
            
            messages.info(request, "You have been successfully logged out.")
        else:
            messages.info(request, "You were not logged in.")
        
        return redirect('auth:login')


# Optional: Add a decorator for rate limiting on other views
from functools import wraps
from django.http import HttpResponseForbidden

def rate_limit(max_requests=10, window=60):
    """
    Generic rate limiting decorator for other views
    Usage: @rate_limit(max_requests=10, window=60)
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            ip = request.META.get('REMOTE_ADDR')
            key = f'rate_limit_{ip}_{view_func.__name__}'
            
            requests = cache.get(key, [])
            now_time = time.time()
            
            # Clean old requests
            requests = [t for t in requests if now_time - t < window]
            
            if len(requests) >= max_requests:
                return HttpResponseForbidden("Too many requests. Please try again later.")
            
            requests.append(now_time)
            cache.set(key, requests, timeout=window)
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator




