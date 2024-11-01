from django.urls import path
from . import views

urlpatterns = [
    path('', views.rules_list, name='rules'),
]
