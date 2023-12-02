# video_upload/tasks.py

from celery import shared_task
from .models import Video, Subtitle
import subprocess
from datetime import datetime, timedelta

@shared_task
def process_video(video_id):
    # Fetch video by ID
    video = Video.objects.get(id=video_id)

    # Define the path for the ccextractor binary
    ccextractor_path = '/path/to/ccextractor'  # Replace with the actual path

    # Run ccextractor to extract subtitles
    command = f"{ccextractor_path} {video.video_file.path} -o subtitles.srt"
    subprocess.run(command, shell=True)

    # Process the generated subtitles file and save to the database
    with open('subtitles.srt', 'r') as file:
        subtitles = file.read().split('\n\n')

        for subtitle_block in subtitles:
            subtitle_lines = subtitle_block.strip().split('\n')

            # Extract timecodes and subtitle text
            try:
                timecode_parts = subtitle_lines[1].split(' --> ')
                start_time = datetime.strptime(timecode_parts[0], '%H:%M:%S,%f').time()
                end_time = datetime.strptime(timecode_parts[1], '%H:%M:%S,%f').time()
                subtitle_text = '\n'.join(subtitle_lines[2:])
            except (ValueError, IndexError):
                # Skip this subtitle if there's an error in parsing
                continue

            # Save subtitle to the Subtitle model
            subtitle = Subtitle.objects.create(
                video=video,
                text=subtitle_text,
                start_time=start_time,
                end_time=end_time
            )

    # Clean up temporary files
    os.remove('subtitles.srt')
