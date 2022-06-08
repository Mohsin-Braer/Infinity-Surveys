"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include 
from register import views as v 
from main import views as vm 
from teamcreation import views as v1
from peerassessment import views as v2
from django.contrib.auth import views as auth_views
from register.views import UserEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    path('dashboard/', vm.dashboard, name="dashboard"),
    path('profile/', UserEditView.as_view(), name="profile"),
    path('', include("main.urls")),
    path('home/', include("main.urls")),
    path('', include("django.contrib.auth.urls")),
    path('teamcreation/', v1.contact_testing, name = "teamcreation"),
    path('peerassessment/', v2.get_PA_results, name = "peerassessment"),
    path('create/', v2.get_PA, name = "peerassessment_creation"),
    path('password/', auth_views.PasswordChangeView.as_view()),
]
