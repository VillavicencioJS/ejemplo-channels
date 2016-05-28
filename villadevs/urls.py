from django.conf.urls import url, include
from django.contrib import admin
from chat import views

urlpatterns = [
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]
