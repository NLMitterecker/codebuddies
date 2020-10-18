from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_share/<int:post_id>', views.post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_details,
        name='post_details')
]