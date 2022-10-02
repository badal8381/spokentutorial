
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('tts/', include('tts.urls')),
    path('videomerge/', include('videomerge.urls')),
]

