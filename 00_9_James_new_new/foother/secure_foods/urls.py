from django.contrib import admin
from django.urls import path
from . import views

app_name = 'secure_foods'

urlpatterns = [
    path('select/<str:ctf_type_name>/', views.select, name='select'),
    # path("example/", views.example, name='example'),
]