
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import UserRegistrationView, UserProfileDetailView, UserProfileEditView
from  django.urls import reverse_lazy
app_name = 'accounts'
urlpatterns = [    
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path('profile/<slug:slug>/',
        UserProfileDetailView.as_view(), name='profile'),
    path('edit-profile/', UserProfileEditView.as_view(), name='update_profile'),
]