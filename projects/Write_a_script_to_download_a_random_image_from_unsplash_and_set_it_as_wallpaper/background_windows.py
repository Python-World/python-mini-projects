from requests import get
import os
import ctypes
import sys

url = "https://source.unsplash.com/random"
file_name = "random.jpg"

def is_64bit():
    return sys.maxsize > 2 ** 32


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
    if is_64bit():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)


if __name__ == "__main__":
    try:
        download(url, file_name)
        setup(file_name)
    except Exception as e:
        print(f"Error {e}")
        raise NotImplementedError
