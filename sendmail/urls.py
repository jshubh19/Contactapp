from django.contrib import admin
from django.conf.urls import url
#from .views import email , success
from . import views

urlpatterns= [
    url(r'^$',views.email, name='email'),
    url(r'^success/',views.success, name='success'),
]