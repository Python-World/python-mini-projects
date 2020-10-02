##  split a video file by given time period

This script will split the video into two files when valid time periods are given.


### Requirements
Install python in the host system
Install [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)

```
pip install ffmpeg-python
``` 

### usage

```python
python videosplitter.py test.mp4 0 50 out1.mp4 out2.mp4
```
OR

```python
python videosplitter.py -h
```

