from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Temporary to reset superuser (REMOVE AFTER USE!)
def reset_superuser(request):
    User = get_user_model()
    email = 'mounica@gmail.com'  # your email
    user, created = User.objects.get_or_create(email=email, defaults={'username': 'mounica'})
    user.set_password('mouni1807')  # CHANGE to your new password
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.save()
    return HttpResponse("Superuser reset! Login at /admin/ with email: mounica@gmail.com and new password.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('reset-superuser/', reset_superuser),  # temporary - remove after use
]