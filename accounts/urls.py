
from django.urls import path, include
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import views as auth_views
from .views import UserRegistrationView, UserProfileDetailView, UserProfileEditView
app_name = 'accounts'
urlpatterns = [    
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='registration/change_password.html',success_url = 'profile/<slug:slug>/'), name="change_password"),
    # path('reset-password/',auth_views.PasswordResetView.as_view(),name=" password_reset"),
    # path('reset-password-sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path('reset-success/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
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