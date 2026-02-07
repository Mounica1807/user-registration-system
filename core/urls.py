from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(email='mouni@gmail.com').exists():
        User.objects.create_superuser(
            email='mouni@gmail.com',
            username='adminnew',
            password='password123' 
        )
        return HttpResponse("Superuser created successfully!")
    return HttpResponse("Superuser already exists.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]