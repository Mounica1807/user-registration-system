from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Admin panel (must be here)
    path('admin/', admin.site.urls),

    # API routes (your registration/login/profile)
    path('api/', include('accounts.urls')),

    # Home page - shows index.html (your registration form)
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]