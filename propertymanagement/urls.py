"""propertymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import  views as homeViews
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    
    path('',homeViews.HomeView.as_view(), name="mainpage"),    
    path('contact-us/',homeViews.ContactView.as_view(), name="contactus"),
    path('success/',TemplateView.as_view(template_name='contact_success.html'), name="success"),
    path('about-us/', homeViews.AboutUsView.as_view(),name="about-us"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('address/', include('address.urls')),
    path('rentals/', include('housing.urls')),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/change_password_form.html'),name='password_change'),
    path('accounts/password_change/done/',auth_views.PasswordChangeDoneView.as_view(), 
        name='password_change_done'),
    path('accounts/password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), 
    name='password_reset_confirm'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html"
    ), name='password_reset'),
    
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# from django.conf.urls import (
# handler400, handler403, handler404, handler500
# )
# handler404 = homeViews.custom_404
# handler500 = homeViews.custom_500