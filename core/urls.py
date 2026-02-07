from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Temporary superuser creation/reset (remove after use!)
def create_superuser(request):
    User = get_user_model()
    email = 'mouni@gmail.com'  # your email
    if User.objects.filter(email=email).exists():
        return HttpResponse("Superuser already exists. Go to /admin/ to login.")
    else:
        User.objects.create_superuser(
            email=email,
            username='mouni',
            password='mouni1807'  # CHANGE THIS PASSWORD NOW!
        )
        return HttpResponse("Superuser created! Login at /admin/")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('create-superuser/', create_superuser),  # temporary line
]