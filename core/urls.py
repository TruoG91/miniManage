from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apartments/<int:pk>/', views.apartments, name='apartments')
]