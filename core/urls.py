from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_superuser(request):
    User = get_user_model()
    email = 'mouni@gmail.com'  # ← change if needed
    if User.objects.filter(email=email).exists():
        return HttpResponse("Superuser with this email already exists. Go to /admin/ to login.")
    else:
        User.objects.create_superuser(
            email=email,
            username='mouni_admin',
            password='mouni12345'  # ← CHANGE THIS PASSWORD to something secure!
        )
        return HttpResponse("Superuser created successfully! You can now login at /admin/")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('create-superuser/', create_superuser),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]