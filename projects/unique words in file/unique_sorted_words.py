#!/usr/bin/env python
import re

# script to fetch unique sorted words from a text file.
list_of_words = []

# Alternate Method to insert file
# filename = input("Enter file name: ")
filename = "test_file.txt"
with open(filename, "r") as f:
    for line in f:
        list_of_words.extend(re.findall(r"[\w']+", line.lower()))


unique_word = set(list_of_words)
print(sorted(unique_word))
