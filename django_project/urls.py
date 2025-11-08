from django.contrib import admin
from django.urls import path
from django_app.views import *

urlpatterns = [
    path ( 'admin/', admin.site.urls ),
    path ( '', index, name='index' ),
    path ( 'about/', about, name='about' ),
    path ( 'company/', company, name='company' ),
    path ( 'contact/', contact, name='contact' ),
    path ( 'design/', design, name='design' ),
    path ( 'news/', news, name='news' )
]