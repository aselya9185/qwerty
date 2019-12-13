"""ada URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('login/',include('registration.urls')),
    path('registrations/',include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('orders/',include('orders.urls')),
    path('products/',include('products.urls')),
    path('mens/',include('mens.urls')),
    path('child/',include('child.urls')),
    path('page/', include('page.urls')),
    path('accessories/', include('accessories.urls')),
    path('sales/',include('sales.urls')),
]\
            + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
            + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
