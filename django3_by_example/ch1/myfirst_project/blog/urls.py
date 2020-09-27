from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.post_list, name='post_list'),
]