from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('rooms/', views.getRooms),
    path('users/', views.getUsers),
    path('rooms/<str:pk>/', views.getRoom),
]
