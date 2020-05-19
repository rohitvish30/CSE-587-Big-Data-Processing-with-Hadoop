#!/usr/bin/env python
# coding: utf-8

# In[15]:


import nltk
#nltk.download("stopwords")
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import re
import sys
import os

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

for words in sys.stdin:#reading the file input
    words= words.strip().split()#first removing the trailing space and then splitting the sentence on each word 
    for word in words:
        word = text_preprocess(word) #to preprocess the data
        if word: #if the process word is valid then print the word with its count
            print('%s\t%s'%(word, 1))


