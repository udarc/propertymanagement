
from django.urls import path, include
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import views as auth_views
from .views import UserRegistrationView, UserProfileDetailView, UserProfileEditView
app_name = 'accounts'
urlpatterns = [    
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
         # User Profile

    path('profile/<slug:slug>/',
        UserProfileDetailView.as_view(), name='profile'),
    path('edit-profile/', UserProfileEditView.as_view(), name='update_profile'),
    # path('change-password/', auth_views.PasswordChangeView.as_view()),
#    path(
#         'change-password/',
#         auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
#     ),
#     path('change_password_done/', password_change_done, name='password_change_done',
#         kwargs={'template_name': 'accounts/change_password_done.html'}),
]