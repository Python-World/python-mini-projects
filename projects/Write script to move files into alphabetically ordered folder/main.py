'''
This script will sort and move the files in the directory
(the alphabetical order).

'apple.txt' --> 'A'
'ryan.txt' --> 'R'
'01010.txt' --> 'Misc'

'''
import os
import shutil

filenames = []


def getfoldername(filename):
    '''
    'Test.txt' --> 't'
    '010.txt' --> 'misc'
    'zebra.txt' --> 'z'
    'Alpha@@.txt' --> 'a'
    '!@#.txt' --> 'misc'
    '''
    if filename[0].isalpha():
        return filename[0].lower()
    else:
        return 'misc'


def readdirectory():
    '''
    read the filename in the current directory and append them to a list
    '''
    global filenames
    for files in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(), files)):
            filenames.append(files)
    filenames.remove('main.py')  # removing script from the file list


# getting the first letters of the file & creating a file in the current_dir
def createfolder():
    '''
    creating a folders
    '''
    global filenames
    for f in filenames:
        if os.path.isdir(getfoldername(f)):
            print("folder already created")
        else:
            os.mkdir(getfoldername(f))
            print('creating folder...')


# moving the file into the proper folder
def movetofolder():
    '''
    movetofolder('zebra.py','z')

    'zebra.py'(moved to) 'z'
    '''
    global filenames
    for i in filenames:
        filename = i
        file = getfoldername(i)
        source = os.path.join(os.getcwd(), filename)
        destination = os.path.join(os.getcwd(), file)
        print(f"moving {source} to {destination}")
        shutil.move(source, destination)


if __name__ == '__main__':
    readdirectory()
    createfolder()
    movetofolder()
