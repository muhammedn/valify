from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_polls, name='list_polls'),
    path('<int:poll_id>', views.show_poll, name='show_poll')

]
