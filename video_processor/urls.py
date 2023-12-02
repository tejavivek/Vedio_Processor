# video_processor/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from video_upload.views import upload_video  # Update the import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('video_upload.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
