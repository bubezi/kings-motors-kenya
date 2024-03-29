"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings
from register import views as v




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', v.register, name="register"),
    path('bye/', v.bye_page, name="bye"),
    path('', include('store.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('', include("django.contrib.auth.urls")),

]





urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





admin.site.site_header = "King's Motors Kenya Admin Panel"
admin.site.site_title = "King's Motors Kenya"
admin.site.index_title = "King's Motors Kenya"