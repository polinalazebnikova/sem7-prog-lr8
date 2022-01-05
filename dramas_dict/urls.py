from django.urls import path

from . import views

urlpatterns = [
    path('', views.drama_table, name='drama_table'),
]