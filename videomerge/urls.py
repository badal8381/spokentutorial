from django.urls import path
from . import views

urlpatterns = [
    path('', views.video, name="videomerge"),
    path('<str:id>/', views.download_video, name='download-video'),
]