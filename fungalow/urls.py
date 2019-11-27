from django.urls import path
from . import views

urlpatterns = [
    path('homes', views.home_list, name='home_list'),
]
