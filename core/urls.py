from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Temporary endpoint to create/reset superuser (REMOVE AFTER USE!)
def create_superuser(request):
    User = get_user_model()
    email = 'mouni@gmail.com'  # ← your email
    if User.objects.filter(email=email).exists():
        return HttpResponse("Superuser already exists. Go to /admin/ to login.")
    else:
        User.objects.create_superuser(
            email=email,
            username='mouni',
            password='mouni123456'  # ← CHANGE THIS to a password YOU WILL REMEMBER
        )
        return HttpResponse("Superuser created! Now login at /admin/")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('create-superuser/', create_superuser),  # temporary line - remove later
]