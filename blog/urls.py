from django.urls import path
from . import views

urlpatterns = [
    path('list', views.post_list, name='post_list'),
    path('cb17_1', views.cb17_1, name='cb17_1')
]