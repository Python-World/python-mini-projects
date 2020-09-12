import os
import shutil
os.chdir("E:\downloads")
#print(os.getcwd())

#check number of files in  directory
files = os.listdir()

#list of extension (You can add more if you want)
extentions = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"]


}


#sort to specific folder depend on extenstions
def sorting(file):
    keys = list(extentions.keys())
    for key in keys:
        for ext in extentions[key]:
            # print(ext)
            if file.endswith(ext):
                return key


#iterat through each file
for file in files:
    dist = sorting(file)
    if dist:
        try:
            shutil.move(file, "../download-sorting/" + dist)
        except:
            print(file + " is already exist")
    else:
        try:
            shutil.move(file, "../download-sorting/others")
        except:
            print(file + " is already exist")

