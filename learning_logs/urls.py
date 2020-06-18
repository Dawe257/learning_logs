from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домащная страница
    path('', views.index, name='index'),
]