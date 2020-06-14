from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about, name='about'),
    path('our_causes', views.causes, name='causes'),
    path('our_blogs', views.blog, name='blog'),
    path('contact_us', views.contact, name='contact'),
    path('login_to_nsss', views.login, name='login'),
    path('register_to_nsss', views.register, name='register'),
    path('donate_to_nsss', views.donate, name='donate'),
    ]