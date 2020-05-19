#!/usr/bin/env python
# coding: utf-8

# In[6]:




import sys
import re
from collections import Counter


def Calculate_label(label_list):
    data = Counter(label_list)
    data.most_common()  # Returns all unique items and their counts
    return data.most_common(1)[0][0]

# Reading mapper's output
for lines in sys.stdin:
    lines=re.sub(r"\s+", "",lines)
    elements = lines.split(';')
    # print(elements[1])
    label_list = elements[1].split(',')
    #print(label_list)
    label_to_pass = []
    for i in label_list:
	try:
	        label_to_pass.append(int(i)) #making the count as int dattype
    	except ValueError:
        	continue
    label = Calculate_label(label_to_pass)
# Printing test data with predicted labels
    #print(elements[0],',',label)
    print("%s - %s"%(elements[0],label))
