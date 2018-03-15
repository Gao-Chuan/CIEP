"""ciep URL Configuration

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
from django.conf.urls import url


from mainPage import views
from encrypt import views as enc_views
from authenticated import views as auth_views
from pns import views as pns_views

urlpatterns = [
    # main page
    url(r'^$', views.home, name='home'),

    # encrypt page
    url(r'^encrypt$', enc_views.home, name='enc_home'),
    url(r'^encrypt/secretkey$', enc_views.secretKey_home, name='enc_secret_home'),
    url(r'^encrypt/publickey$', enc_views.publicKey_home, name='enc_public_home'),

    url(r'^admin/', admin.site.urls),
]
