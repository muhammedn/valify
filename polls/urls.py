from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_polls, name='list_polls'),

]
