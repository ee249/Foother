from django.contrib import admin
from django.urls import path
from . import views

app_name = 'mains'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:emotion_id>/', views.result, name='result'),
    path('<str:food_name>/select', views.select, name='select'),
    path("example/", views.example, name='example'),
]
