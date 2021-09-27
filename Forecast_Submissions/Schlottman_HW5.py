#Assignmnent_5
#By: Jason Schlottman 
#Week5: Pandas Dataframe
#Course: HAS Tools: Tools for Data Handling and Analysis in Water, Weather, & Climate
#Date: 9/21/2021


#The code below is a modified version based on the provided starter code developed by Dr. Laura Condon
# %%
# Import the necessary modules 
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# This 'filename' variable refers to the streamflow data (flow in cfs) acquired from USGS daily data from the site: '09506000 Verde River Near Camp Verde'.
#This streamflow data ranges from 01-01-1989 to 09-22-2021. 
filename = 'streamflow_week5.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week5.txt'

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep = '\t', skiprows=30,
        names =['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
#The Section below defines the functions necessary to return desired info to answer assignment prompts.
#Functions Section:

# The function below prints each row and column of data in the file.
'print(data)'

#Question 1:

#The function below returns a description which also includes quantitative values of the 'flow' column including min,mean,max,std,quantiles & data type
'data.info()'

#data['day'].describe()
#data['agency_cd'].describe()
#data['site_no'].describe()
#data['datetime'].describe()
#data['flow'].describe()
#data['code'].describe()
#data['year'].describe()
#data['month'].describe()

#Question 2:

data['flow '].describe()

#'data['flow'].describe()'

#Question 3:

#The function below utilizes the groupby() and describe() methods to return a tabular set of data with the returned values grouped by month which describe common flow parameters.
#data.groupby(['month'])['flow'].describe()

#Question 4:
#The code below utilizes the head() and tail() functions which retrive the first and last 'n' rows chosen and allow us to sort the datetime and flow parameters together with the highest and lowest 5 values shown. 

'''
{
tab=data[['datetime', 'flow']].sort_values(by='flow', ascending=False)
hi5=tab.head()
low5=tab.tail()

vals=[hi5, low5]
dat=pd.concat(vals)
dat
}
'''

#Question 5:

#First define arrays for the minimum and maximum values and associated times.

'''
{
min_ray=np.array([])
max_ray=np.array([])
#The lines below form a for loop and sorts each value and utilizes the head() function to pull the top values asssociated with the month, as well as in ascending order, then appends.
for month in data['month']:
        sort1=data.sort_values(by='flow', ascending=True).head(1)
        min_ray.append(sort1)
        sort2=data.sort_values(by='flow', ascending=False).head(1)
        max_ray.append(sort2)
}
'''

data.groupby(["year", "month"])[["flow"]].describe()

#Question 6:

'''
{
#The code below defines a range of returns which are output in an array if their associated flow values fall within 10% of the week 1 forecast value meaning they're between 121.5 and 148.5 cfs.
wk1_fore=135
lo=wk1_fore*0.9
hi=wk1_fore*1.1
array=data[(data['flow']>=lo) & (data['flow']<=hi)]
a_date=array['datetime']
#the function below gives a count of the total number of returned dates which fall within the range. when defined as true
a_date.count()
a_date.to_csv(index=False)
}
'''

# %%

