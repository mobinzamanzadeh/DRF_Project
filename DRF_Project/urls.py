"""DRF_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from dj_rest_auth.views import PasswordResetConfirmView
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from api.views import RevokeToken


urlpatterns = [
    path('/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token-auth/', obtain_auth_token),
    # path('api/revoke/', RevokeToken.as_view()),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm')
]
