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
from . import  views as homeViews
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
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
