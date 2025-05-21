from django.urls import path
from . import views

urlpatterns = [
    path('', views.open_mic_list, name='open_mic_list'),
    path('add-mic/', views.add_mic, name='add_mic'),
] 