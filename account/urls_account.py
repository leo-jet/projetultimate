from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from account import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)