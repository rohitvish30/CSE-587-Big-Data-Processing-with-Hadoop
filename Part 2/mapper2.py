#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk
#nltk.download("stopwords")
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import re
import sys

word_array=[]

def cleantxt(word_array,index): # printing the tri-gram 
    if(index==0 and len(word_array)>=3): 
        print("%s\t%s"%(("$_"+word_array[index+1]+"_"+word_array[index+2]),"1"))
    elif(index==len(word_array)-1 and len(word_array)>=3):
        print("%s\t%s"%((word_array[index-2]+"_"+word_array[index-1]+"_$"),"1"))
    elif((index==1 or index==len(word_array)-2) and len(word_array)>=3):
        print("%s\t%s"%((word_array[index-1]+"_$_"+word_array[index+1]),"1"))
    else:
        print("%s\t%s"%((word_array[index-2]+"_"+word_array[index-1]+"_$"),"1"))
        print("%s\t%s"%((word_array[index-1]+"_$_"+word_array[index+1]),"1"))
        print("%s\t%s"%(("$_"+word_array[index+1]+"_"+word_array[index+2]),"1"))

def text_preprocess(word):
    #stop_words = set(stopwords.words('english'))
    word = word.lower() # making all the letters to lower case
    processed_word = [] 
    #if word not in stop_words: #removing all the stopwords like is, the ,on,a etc.
    pattern = re.compile('[\w\d\'-]') #creating a regular expression that allows only words, letters, " ' " and " -"
    for i in range(0, len(word)):
        if pattern.match(word[i]): #applying the regular expression to each word
            processed_word.append(word[i]) #appending each word
    return ''.join(processed_word) #combining all letters of a word

def wordFunc(word_array): #function for matching the given keywords for generating tri-grams
    new_words=[]
    count=0;
    for i in range(len(word_array)):
        if(word_array[i]=="science" or word_array[i]=="sea" or word_array[i]=="fire"):
            (cleantxt(word_array,i))
    
for words in sys.stdin:
    words = words.strip().split() #first removing the trailing space and then splitting the sentence on each word 
    for word in words:
        clean_word=text_preprocess(word)#to preprocess the data
	#print(clean_word)
        if clean_word:
            word_array.append(clean_word)#to append in the word_array all the clean words
wordFunc(word_array)

