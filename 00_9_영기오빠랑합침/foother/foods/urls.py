from django.contrib import admin
from django.urls import path
from . import views

app_name = 'foods'

urlpatterns = [
    path('', views.main, name='main'),
    path('result/<str:food_ctg>/', views.result, name='result'),
    path('result1/', views.result1, name='result1'),
    path('select/<str:food_name>/', views.select, name='select'),
    # path("example/", views.example, name='example'),
]