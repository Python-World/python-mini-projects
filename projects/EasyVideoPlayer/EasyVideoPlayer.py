import cv2
import os
from pathlib import Path
from ffpyplayer.player import MediaPlayer


# User input for the name of the image file.
video_name = input("Name of the video file that you want to play:    ")

# User input for the path of the image file.
video_directory_guess = input("Directory that may contain the video:    ")


# This function finds your file. If you don't know the directory just type '/'
def find_the_video(file_name, directory_name):
    files_found = []
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if(file_name == name):
                file_path = os.path.join(path, name)
                files_found.append(file_path)

    print(files_found)
    return files_found[0]  # Return the path.


# Initialize the path of the image file.
video_directory = Path(find_the_video(video_name, video_directory_guess))

# Initialize the parent directory of the image path.
new_working_directory = video_directory.parent

# Change the working directory of the script.
os.chdir(new_working_directory)


video_path = find_the_video(video_name, video_directory_guess)


def PlayVideo(video_path):

    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)

    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()


PlayVideo(video_path)
