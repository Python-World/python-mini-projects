import os
import shutil
<<<<<<< HEAD

os.chdir("E:\\downloads")
# print(os.getcwd())

# check number of files in  directory
files = os.listdir()

# list of extension (You can add more if you want)
=======
os.chdir("E:\downloads")
#print(os.getcwd())

#check number of files in  directory
files = os.listdir()

#list of extension (You can add more if you want)
>>>>>>> 760b764f0e43d93842442ba57e745ef195a27d42
extentions = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
<<<<<<< HEAD
    "documents": [".pdf", ".docx", ".csv",
                  ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"],
}


# sort to specific folder depend on extenstions
=======
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"]


}


#sort to specific folder depend on extenstions
>>>>>>> 760b764f0e43d93842442ba57e745ef195a27d42
def sorting(file):
    keys = list(extentions.keys())
    for key in keys:
        for ext in extentions[key]:
            # print(ext)
            if file.endswith(ext):
                return key


<<<<<<< HEAD
# iterate through each file
=======
#iterat through each file
>>>>>>> 760b764f0e43d93842442ba57e745ef195a27d42
for file in files:
    dist = sorting(file)
    if dist:
        try:
            shutil.move(file, "../download-sorting/" + dist)
<<<<<<< HEAD
        except Exception:
=======
        except:
>>>>>>> 760b764f0e43d93842442ba57e745ef195a27d42
            print(file + " is already exist")
    else:
        try:
            shutil.move(file, "../download-sorting/others")
<<<<<<< HEAD
        except Exception:
=======
        except:
>>>>>>> 760b764f0e43d93842442ba57e745ef195a27d42
            print(file + " is already exist")
