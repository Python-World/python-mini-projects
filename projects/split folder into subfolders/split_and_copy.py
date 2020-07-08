import glob
import os
from shutil import copy2
import sys


def get_files(path):
    '''
    return a list of files avialable in given folder
    '''
    files = glob.glob(f'{path}/*')
    return files


def getfullpath(path):
    '''
    Return absolute path of given file
    '''
    return os.path.abspath(path)


def copyfiles(src, dst):
    '''
    This function copy file from src to dst
    if dst dir is not there it will create new
    '''
    if not os.path.isdir(dst):
        os.makedirs(dst)
    copy2(src, dst)


def split(data, count):
    '''
    Split Given list of files and return generator
    '''
    for i in range(1, len(data), count):
        if i + count-1 > len(data):
            start, end = (i-1, len(data))
        else:
            start, end = (i-1, i+count-1)
        yield data[start:end]


def start_process(path, count):
    files = get_files(path)
    splited_data = split(files, count)

    for idx, folder in enumerate(splited_data):
        name = f'data_{idx}'
        for file in folder:
            copyfiles(getfullpath(file), getfullpath(name))


if __name__ == "__main__":
    '''
    driver code
    To run this script
    python split_and_copy.py <input folder path> <20>
    '''

    if len(sys.argv) != 3:
        print("Please provide correct parameters \
        \npython split_and_copy.py <input folder path> <count>")
        sys.exit(0)

    if len(sys.argv) == 3:
        path = sys.argv[1]
        if os.path.isdir(path):
            count = sys.argv[2]
            start_process(path, int(count))
        else:
            print('Given directory name is not an valid directory')
    else:
        print('Wrong paramter are provided')
