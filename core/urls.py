from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import RegisterView, ProfileView
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# TEMPORARY FUNCTION - only for creating/resetting superuser (REMOVE AFTER USE!)
def create_superuser(request):
    User = get_user_model()
    email = 'mouni@gmail.com'  # your email
    if User.objects.filter(email=email).exists():
        return HttpResponse("Superuser already exists. Go to /admin/ to login.")
    else:
        User.objects.create_superuser(
            email=email,
            username='mouni',
            password='mouni1807'  # CHANGE THIS TO A SECURE PASSWORD YOU WILL REMEMBER
        )
        return HttpResponse("Superuser created! Now login at /admin/")

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create-superuser/', create_superuser),  # temporary line - delete after use
]