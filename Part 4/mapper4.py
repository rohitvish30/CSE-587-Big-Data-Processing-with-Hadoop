#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sys

# Reading input datasets from command line
for line in (sys.stdin):
    line = line.strip()

    line = line.split('\t')


    employee_Id = "-1"
    name = "-1"
    salary = "-1"
    country = "-1"
    code = "-1"

# Differentiating which line is from which dataset by checking the number of columns
    if len(line) ==2:
        employee_Id = line[0]
        name = line[1]

    else:
        employee_Id = line[0]

        salary = line[1]
        country = line[2]
        code = line[3]
# Printing data collectively from two dataset
    print(employee_Id,';',name,';',salary,';',country,';',code)


