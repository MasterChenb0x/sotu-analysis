#!/usr/bin/env python3

import string
import sys

if len(sys.argv) != 2:
    raise ValueError('Please enter a speech file to analyze')

speech = sys.argv[1]
print(speech)

with open(f'{speech}', 'r', encoding='utf8') as speech_file:
    speech_list = speech_file.readlines()

word_dict = {}
table = str.maketrans('', '', string.punctuation)

for line in speech_list:
    words = line.split()
    for word in words:
        word = word.translate(table)
        word = word.lower()
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
sort_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=False)
for i in sort_words:
    print(i[0], i[1])

# print(word_dict)