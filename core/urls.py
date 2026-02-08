from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # This line makes /admin/ work
    path('admin/', admin.site.urls),

    # Your API routes
    path('api/', include('accounts.urls')),

    # Home page (your registration form)
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]