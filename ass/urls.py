from django.urls import path
from . import views

app_name = 'ass'
urlpatterns = [
    path('', views.index, name='index'),
]