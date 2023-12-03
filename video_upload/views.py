from celery.result import AsyncResult
from .forms import VideoUploadForm
from .tasks import process_video
from django.shortcuts import render 
from django.views.generic import TemplateView

class upload_video(TemplateView):
    template_name = "upload_video.html" 
    def post(self, request):
        # if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            # task1 = add.delay(2,3)
            # print(task1,'-----------------------')
            task = process_video.delay(video.id)  # Trigger background video processing
            print(task, '----------------taskasasalnkfjsd================')
            try:
                result = task.get(timeout=10)  # Adjust the timeout as needed
            except Exception as e:
                print(e, "eeeeeeeeeeeeeeeeeeeee")
                # Log the exception or handle it appropriately
                error_message = str(e)
                return render(request, 'processing_error.html', locals())
            return render(request, 'processing_status.html', {'video_id': video.id})
        else:
            form = VideoUploadForm()
            return render(request, 'upload_video.html', {'form': form})