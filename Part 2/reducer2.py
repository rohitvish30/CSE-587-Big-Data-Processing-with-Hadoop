#!/usr/bin/env python
# coding: utf-8

# In[6]:

import operator
from operator import itemgetter
import sys
import collections

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

sorted_by_value = sorted(word_count_dict.items(), key=operator.itemgetter(1),reverse=True)[:10] #sort by values i.e top 10 values in descending order 
sorted_dict = collections.OrderedDict(sorted_by_value) 
for word in sorted_dict.keys(): #printing the word and its value
    print("%s\t%s"%(word,sorted_dict[word]))

            

