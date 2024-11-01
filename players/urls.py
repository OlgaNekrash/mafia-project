from django.urls import path
from . import views

urlpatterns = [
    path('', views.players_list, name='players'),
    path('players/<int:pk>/', views.player_detail, name='player_detail'),
]
