from django.contrib import admin
from django.urls import path, include
import wordcount.views

urlpatterns = [
    path('', wordcount.views.home, name="home"),
    path('about/', wordcount.views.about, name="about"),
    path('count/', wordcount.views.count, name="count"),
]