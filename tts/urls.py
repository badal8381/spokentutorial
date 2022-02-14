from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="tts"),
    path('<str:id>/', views.download_speech, name='download-audio'),
]
