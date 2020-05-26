from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('get_result/', views.get_result, name='get_result'),
]