#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sys
import re

emp_dict = {}
emp_details_dict = {}

# Reading mapper output
for line in sys.stdin:
    line=re.sub(r"\s+", "",line)

    employee_Id,name,salary,country,code = line.split(';')

# Discarding the header here
    if (employee_Id=='EmployeeID'):
        continue
    # Checking which line is from which dataset and building corresponding dictionary to join
    if (name ==str(-1)):
        emp_details_dict[employee_Id] = [salary,country,code]
    else:
        emp_dict[employee_Id]=name

# printing the header
print('{:<20s} {:<20s} {:<20s} {:<35s} {:<20s}'.format("Employee ID", "Name", "Salary", "Country", "Passcode"))
# Performing the join operation
for employee_Id in emp_details_dict.keys():
    name=emp_dict[employee_Id]
    salary = emp_details_dict[employee_Id][0]
    country = emp_details_dict[employee_Id][1]
    code = emp_details_dict[employee_Id][2]
# Printing final output after join
    print('{:<20s} {:<20s} {:<20s} {:<35s} {:<20s}'.format(employee_Id, name, salary, country, code))




