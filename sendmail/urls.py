from django.contrib import admin
from django.conf.urls import url
#from .views import email , success
from . import views
from django.conf.urls.static import  static
from django.conf.urls.static import settings

urlpatterns= [
    url(r'^$',views.email, name='email'),
    url(r'^success/',views.success, name='success'),
    url(r'^signup/', views.register, name='register'),
    url(r'^signup/completed/', views.regcompleted, name='regcompleted'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT )

#urlpatterns += staticfiles_urlpatterns()