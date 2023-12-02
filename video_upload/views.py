# video_upload/views.py

from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from .tasks import process_video_task  # Import your Celery task if needed
from .models import Video


def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            process_video_task.delay(video.id)  # Trigger background video processing
            return render(request, 'processing_status.html', {'video_id': video.id})
    else:
        form = VideoUploadForm()

    return render(request, 'upload_video.html', {'form': form})
