import datetime
import os
import re
import subprocess


def rename_files_with_whitespaces(cd, files, extra_path=""):
    for file in files:
        if " " in file:
            renamed_file = file.replace(" ", "_")
            os.rename(os.path.join(cd, extra_path, file), os.path.join(cd, extra_path, renamed_file))


def clean_filename(file):
    return ' '.join(map(str.capitalize, file[:-4].split('_')))


def set_alarm():
    stop = False
    error = True
    while error:
        user_set_time = ":".join(map(lambda x: str(x).zfill(2), input("\nSet the alarm time (e.g. 01:10): ").split(":")))

        if re.match(r"^[0-9]{2}:[0-9]{2}$", user_set_time):
            playback_time = f"{user_set_time}:00.000000"
            error = False
        else:
            print(">>> Error: Time format invalid! Please try again!\n")
            
    cd = os.path.dirname(os.path.realpath(__file__))
    musics_path = os.path.join(cd, "musics")
    
    rename_files_with_whitespaces(cd, os.listdir(musics_path), "musics")

    musics = os.listdir(musics_path)
    if len(musics) < 1:
        print(">>> Error: No music in the musics folder! Please add music first!\n")
        exit()

    elif len(musics) == 1:
        print(">> Alarm music has been set default --> " + clean_filename(musics[0]))
        selected_music = musics[0]
    
    else:
        error = True
        while error:
            try:
                print("\nSelect any alarm music:\n")
                for i in range(1, len(musics) + 1):
                    print(f"{i}. {clean_filename(musics[i - 1])}")
                    
                user_input = int(input("\nEnter the index of the listed musics (e.g. 1): "))
                selected_music = musics[user_input - 1]
                print(">> Alarm music has been set --> "+ clean_filename(selected_music))
                error = False

            except:
                print(">>> Error: Invalid Index! Please try again!\n")
    
    print(f"\n>>> Alarm has been set successfully for {user_set_time}! Please dont close the program! <<<")
    while stop == False:
        current_time = str(datetime.datetime.now().time())
        if current_time >= playback_time:
            stop = True
            subprocess.run(('cmd', '/C', 'start', f"{cd}\\musics\\{selected_music}"))
            print(">>> Alarm ringing! Closing the program!! Bye Bye!!! <<<")

def display_header(header):
    print("")
    print("###########################".center(os.get_terminal_size().columns))
    print(f"###### {header} ######".center(os.get_terminal_size().columns))
    print("###########################".center(os.get_terminal_size().columns))

if __name__ == "__main__":
    display_header("Alarm Program")
    set_alarm()