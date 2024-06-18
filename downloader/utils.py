# Import the YouTube class from the pytube module to work with YouTube videos
from pytube import YouTube

# Import tkinter library for creating GUI applications
import tkinter as tk

# Import filedialog module from tkinter for creating file dialogs
from tkinter import filedialog

# Import tqdm library for displaying progress bars
from tqdm import tqdm

# Define a function to download a video from YouTube
def download_video(url, save_path):
    try:
        # Create a YouTube object by passing the URL of the video
        yt = YouTube(url)

        # Filter the available streams to include only those with progressive download and mp4 extension
        streams = yt.streams.filter(progressive='2160p', file_extension='mp4')

        # Get the highest resolution stream
        highest_res_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        

        # Download the video to the specified save path
        highest_res_stream.download(output_path=save_path)

        # Print a success message
        print('Video downloaded successfully')

    # Handle exceptions
    except Exception as e:
        # Print any error that occurs during the download process
        print(e)


