import re

list_of_words = []

# Alternate Method to insert file
# file = input("Enter file name: ")
# with open(file, "r") as f:
with open("text_file.txt", "r") as f:
    for line in f:
        list_of_words.extend(re.findall(r"[\w']+", line))

unique_word = set(list_of_words)
print(sorted(unique_word))


