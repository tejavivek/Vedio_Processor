# video_upload/forms.py

from django import forms
from .models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'file']  # Add other fields as needed
