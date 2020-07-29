from requests import get
import os
import ctypes
import argparse

url = "https://source.unsplash.com/random"
filename = "random.jpg"
parser = argparse.ArgumentParser(description="Change the Desktop Background")
parser.add_argument('version',type = str,help="Windows Version (32 or 64)")
args = parser.parse_args()

def download(url, file_name):
    '''
    downloading the file and saving it
    '''
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


def setup(pathtofile,version):
    name_of_file = pathtofile
    path_to_file = os.path.join(os.getcwd(), name_of_file)
    SPI_SETDESKWALLPAPER = 20
    if version == "32":
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)
    elif version == "64":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)


if __name__ == "__main__":
    try:
        download(url, filename)
        setup(filename,args.version)
    except Error as e:
        raise NotImplementedError
