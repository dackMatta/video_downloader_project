from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoForm
from .utils import download_video

# Define your view function
def download_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            save_dir = form.cleaned_data['save_dir']  # Assuming you have a field for save directory
            try:
                download_video(video_url, save_dir)
                return HttpResponse('Video downloaded successfully!')
            except Exception as e:
                return HttpResponse(f'Error downloading video: {str(e)}')
    else:
        form = VideoForm()
    return render(request, 'downloader/download.html', {'form': form})



