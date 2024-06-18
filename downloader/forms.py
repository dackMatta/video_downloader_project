# forms.py
from django import forms

class VideoForm(forms.Form):
    RESOLUTION_CHOICES = [
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
        ('1440p', '1440p'),
        ('2160p', '2160p (4K)'),
        ('4320p', '4320p (8K)')
    ]

    video_url = forms.URLField(label='YouTube Video URL', max_length=200)
    save_dir = forms.CharField(label='Save Directory Path', max_length=200)
    resolution = forms.ChoiceField(label='Resolution', choices=RESOLUTION_CHOICES)



