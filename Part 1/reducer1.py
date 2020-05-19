#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sys
word_count_dict={}


for words in sys.stdin:# reading the mapper input
    words = words.strip() #removing the trailing space if any
    word,count=words.split('\t',1) #splitting the input into word and count
    try:
        count=int(count) #making the count as int dattype
    except ValueError:
        continue
    
    if word not in word_count_dict:#if word i.e key not present in dictonary create the word as its keyand count as its value
        word_count_dict[word]=count
    else:
        word_count_dict[word]=word_count_dict[word]+count#if already exist then add the new count

for word in sorted(word_count_dict.keys()):# print each word with its total count sorted by its key
    print("%s\t%s"%(word,word_count_dict[word]))
       

