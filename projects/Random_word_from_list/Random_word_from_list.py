import sys
import random

if sys.argv[1:]:
    filename = sys.argv[1] # check if filename is supplied as a command line argument
else:
    filename = input("What is the name of the file? (extension included): ")

try:
    file = open(filename)
except:
    print("File doesn't exist!") # handle exception
    exit()

num_lines = sum(1 for line in file if line.rstrip()) # get number of lines

random_line = random.randint(0, num_lines) # generate a random number between possible interval

file.seek(0) # re-iterate from first line

for i, line in enumerate(file):
    if i == random_line:
        print(line.rstrip()) # rstrip removes any trailing newlines :)
        break
