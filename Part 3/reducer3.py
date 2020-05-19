#!/usr/bin/env python
# coding: utf-8

# In[6]:

import re
import sys


word_with_list_of_doc = {} #empty dictionary to create
for line in sys.stdin: #taking the file input
	(word,filename) = line.strip().split('\t') #splitting the input into words and its filename
	if word not in word_with_list_of_doc:# if word i.e key not present in dictoonary append the key with its value as filename
		word_with_list_of_doc[word] = []
		word_with_list_of_doc[word].append(filename)
	elif filename not in word_with_list_of_doc[word]:#if word i.e key exist append the new filename
		word_with_list_of_doc[word].append(filename)

for word, filename in word_with_list_of_doc.items():
    print("%s : %s"%(word,','.join(filename))) # printing the output as word : filename1,filename2,filename3

              


