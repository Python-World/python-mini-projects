import zipfile
import sys
import os


# compress file function
def zip_file(file_path):
    compress_file = zipfile.ZipFile(file_path + '.zip', 'w')
    compress_file.write(path, compress_type=zipfile.ZIP_DEFLATED)
    compress_file.close()


# Declare the function to return all file paths of the particular directory
def retrieve_file_paths(dir_name):
    # setup file paths variable
    file_paths = []

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dir_name):
        for filename in files:
            # Create the full file path by using os module.
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)

    # return all paths
    return file_paths


def zip_dir(dir_path, file_paths):
    # write files and folders to a zipfile
    compress_dir = zipfile.ZipFile(dir_path + '.zip', 'w')
    with compress_dir:
        # write each file separately
        for file in file_paths:
            compress_dir.write(file)


if __name__ == "__main__":
    path = sys.argv[1]

    if os.path.isdir(path):
        files_path = retrieve_file_paths(path)
        # print the list of files to be zipped
        print('The following list of files will be zipped:')
        for file_name in files_path:
            print(file_name)
        zip_dir(path, files_path)
    elif os.path.isfile(path):
        print('The %s will be zipped:' % path)
        zip_file(path)
    else:
        print('a special file(socket,FIFO,device file), please input file or dir')
