import re

# script to fetch unique sorted words from a text file.
list_of_words = []

# Alternate Method to insert file
# filename = input("Enter file name: ")
filename = "text_file.txt"

with open(filename, "r") as f:
    for line in f:
        # if case is ignored then Great and great are same words
        list_of_words.extend(re.findall(r"[\w]+", line.lower()))
        # else use this alternate method:
        # list_of_words.extend(re.findall(r"[\w]+", line))

        
# Creating a dictionary to store the number of occurence of a word
unique = {}
for each in list_of_words:
    if each not in unique:
        unique[each] = 0
    unique[each] += 1
 
# Creating a list to sort the final unique words
s = []

# If occurence of a word(val) is 1 then it is unique
for key, val in unique.items():
    if val == 1:
        s.append(key)
        
print(sorted(s))
    

