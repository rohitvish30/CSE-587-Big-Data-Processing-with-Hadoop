#!/usr/bin/env python
# coding: utf-8

# In[6]:

import nltk
#nltk.download("stopwords")
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import re
import sys
import os

def find_filename():
	filename = os.environ['map_input_file'] #this will give entire filepath with filename which is the current input
	split_directory = filename.split('/') # taking each directory name separately
	filename = split_directory[len(split_directory) - 1] # to give the final filename
	return filename

def text_preprocess(word):
    stop_words = set(stopwords.words('english'))
    word = word.lower() # making all the letters to lower case
    processed_word = [] 
    if word not in stop_words:#removing all the stopwords like is, the ,on,a etc.
        pattern = re.compile('[\w\d\'-]') #creating a regular expression that allows only words, letters, " ' " and " -"
        for i in range(0, len(word)):
            if pattern.match(word[i]): #applying the regular expression to each word
                processed_word.append(word[i]) #appending each word
        return ''.join(processed_word) #combining all letters of a word

for words in sys.stdin: # reading input
	words = words.strip().split() #first removing the trailing space and then splitting the sentence on each word 
	for word in words:
		filename = find_filename() #to get the current file name
		word = text_preprocess(word) #to preprocess the data
		if word: #if the process word is valid then print the word with its current filename
			print('%s\t%s'%(word, filename))

