# Get video resolutions from Youtube
from pytube import YouTube
vid_url = "https://youtu.be/klZNvJArVSE"
vid_obj = YouTube(vid_url)
stream = vid_obj.streams.get_highest_resolution()
vid_obj.streams.all()


