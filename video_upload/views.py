from celery.result import AsyncResult

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            task = process_video_task.delay(video.id)  # Trigger background video processing

            # Add error handling for Celery task
            try:
                result = task.get(timeout=30)  # Adjust the timeout as needed
            except Exception as e:
                # Log the exception or handle it appropriately
                return render(request, 'processing_error.html', {'error_message': str(e)})

            return render(request, 'processing_status.html', {'video_id': video.id})
    else:
        form = VideoUploadForm()

    return render(request, 'upload_video.html', {'form': form})
