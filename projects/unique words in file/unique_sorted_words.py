#!/usr/bin/env python

# script to fetch unique words from a text file in sorted way.
list_of_words = []
with open("test_file.txt", "r") as f:
    for line in f:
        list_of_words.extend(line.strip().lower().split())

unique_word = set(list_of_words)
print(sorted(unique_word))
