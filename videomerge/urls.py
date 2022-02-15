from django.urls import path
from . import views

urlpatterns = [
    path('', views.video, name="videomerge"),
    path('download/<str:id>/', views.download_video, name='download-video'),
    path('preview/<str:id>/', views.preview_video, name='preview-video'),
]