from django.conf.urls import url
# from django.contrib import admin
from . import views 
urlpatterns = [
    url(r'^$', views.index),
    url(r"^process_money$", views.process_money)
]