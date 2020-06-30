from django.urls import path
from . import views


app_name = 'maps'


urlpatterns = [
    path('review/create/', views.review, name='review'),
    path('<str:username>/review/profile/', views.profile, name='profile'),
]