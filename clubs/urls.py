from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_list, name='clubs'),
    path('<int:club_id>/', views.club_detail, name='club_detail'),
]
