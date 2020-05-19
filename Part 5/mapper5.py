#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sys
import pandas as pd
import numpy as np


# Reading Train dataset
train_data = pd.read_csv("/home/cse587/Assignment2/Train.csv", delimiter = ",")
# Assigning training labels
labels =train_data.iloc[:,-1]
train_data=train_data.iloc[:,:-1]
k =10

inputval_set = []
features_set = []

# Reading test dataset
for lines in sys.stdin:
    lines = lines.strip()
    if lines.split(',')[0]=='0':
        continue

    else:
        inputval = lines.split(',')
        inputval_set.append(inputval)

X_test= pd.DataFrame(inputval_set)

X_test_array = X_test.values
X_test_array = X_test_array.astype(np.float)
# print(X_test_array)
X_train_array = train_data.values
X_train_array = X_train_array.astype(np.float)

# Calculating euclidean distance
def calc_sorted_dist(x_test,x_train):
    distance=np.linalg.norm((np.array(x_test))-(np.array(x_train)))
    return distance

# Predicting test labels
def _predict(x_test,X_train_array):
    dist=[calc_sorted_dist(x_test,x_train) for x_train in X_train_array]
    top_k_indices=np.argsort(dist)[:k]
    k_nearest_labels=[labels[i] for i in top_k_indices]
    row_new=','.join(str(x) for x in x_test)
    labels_new=",".join(str(y) for y in k_nearest_labels)
    # print('%s\t%s'%(row_new, labels_new))
    print(row_new+";"+labels_new)


for x_test in X_test_array:
    _predict(x_test,X_train_array)
