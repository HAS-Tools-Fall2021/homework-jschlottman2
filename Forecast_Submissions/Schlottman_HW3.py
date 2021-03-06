# Assignment_3: Lists
#Jason Schlottman
#Date: 9/07/2021

# > HW3 file based on the provided 'Starter code for assignment 3' supplied by Dr. Condon:

# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
#path="C:\Users\jschl\OneDrive\Documents\HAS_Tools\homework-jschlottman2\data\streamflow_week3.txt"
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections.

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework.
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
print(min(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))

# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify

#Temporarily 'commented out':

for i in range(len(flow)):
        if flow [i] > 0 and month[i] == 9:
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(ilist)

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified
# in the ilist
subset = [flow[j] for j in ilist]

#if month == 9:
#        print(len(flow))

#print(type(flow))
#print(type(year))
#print(type(month))
#print(type(day))

#print(len(flow))
#print(len(year))
#print(len(month))
#print(len(day))

#if month == 9:
#        print(flow) 
# %%
