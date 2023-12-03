# video_upload/urls.py

from django.urls import path
from .views import upload_video

urlpatterns = [
    path('upload/', upload_video.as_view(), name='upload_video'),
    # Add other URLs specific to video_upload app if needed
]
