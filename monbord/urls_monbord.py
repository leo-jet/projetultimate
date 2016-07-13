from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from monbord import views

urlpatterns = [
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^maths/complexes$', views.complexes, name='complexes'),
    url(r'^index$', views.index, name='index'),
    url(r'^room$', views.chatroom, name='room'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)