import os
import zipfile
import sys
import argparse

# Code to add the cli
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--zippedfile", required=True, help="Zipped file")
args = vars(parser.parse_args())

#Catching the user defined zip file
zip_file = args['zippedfile']

file_name = zip_file

#To check if the entered zip file is present in the directory
if os.path.exists(zip_file) == False:
    sys.exit("No such file present in the directory")

#Function to extract the zip file
def extract(zip_file):
    file_name = zip_file.split(".zip")[0]
    if zip_file.endswith(".zip"):
        
        #Will use this to save the unzipped file in the current directory
        current_working_directory = os.getcwd()
        new_directory = current_working_directory + "/" + file_name
        #Logic to unzip the file
        with zipfile.ZipFile(zip_file, 'r') as zip_object:
            zip_object.extractall(new_directory)
        print("Extracted successfully!!!")
    else:
        print("Not a zip file")

extract(zip_file) 
