
#Assignmnent_6
#By: Jason Schlottman 
#Week6: AR Plots
#Course: HAS Tools: Tools for Data Handling and Analysis in Water, Weather, & Climate
#Date: 10/04/2021


#The code below is a modified version based on the provided starter_code developed by Dr. Laura Condon
# %%
# Import modules:
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# %%
# ** MODIFY **
# Path defined to call data from file source:
filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)


# %%
# Reading data into pandas dataframe:
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to: year, month, day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %% 
#Plots:

# 1. Observed Daily Flow from 2010 to 2020
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], color='orange')
ax.set(title="A Decade of Observed Flow", xlabel="Date", 
        ylabel="Daily Average Flow [cfs]", yscale='log',
        xlim=[datetime.date(2010, 1, 1),
        datetime.date(2020, 12, 21)])
plt.show()

 #2. Bar plot displaying flow for the 2nd half of July, a common 'heavy-flow' monsoon period.
fig, ax = plt.subplots()
ax.bar(data['datetime'], data['flow'])
ax.set(title='Flow for 2nd Half of July, 2020', xlabel="Date",
        ylabel="Observed Flow (cfs)", 
        xlim=[datetime.date(2020, 7, 15), datetime.date(2020, 7, 31)],
        ylim=[110, 220])
plt.show()

#3 Boxplot of flows since 2000 from November 1-10: 
mon_time = data[(data['month'] == 11) & (data['year'] >=2000)]
mon_days = mon_time[(mon_time['day'] >=1) & (mon_time['day'] <=10)]

fig, ax = plt.subplots()
ax= sns.boxplot(x=mon_days['day'], y='flow', data=data, linewidth=0.5, color='teal')
ax.set(xlabel='Days of November', ylabel='Observed Flow (cfs)', yscale='log')
plt.show()

# 4. Line plot which displays December flows from 2000-2010 to show Winter Rains with plasma color palette.
mypal = sns.color_palette('plasma', 12)
mypal
col = 0
fig, ax = plt.subplots()
for i in range(2000, 2010):
        plot_data=data[(data['year']==i) & (data['month']==12)]
        ax.plot(plot_data['day'], plot_data['flow'],
                color=mypal[col], label=i)
        ax.set(xlabel='Day', ylabel='Observed Flow (cfs)', yscale='log')
        col = col+1

#5. Scatter plot for flow in July and December for events from 1990-2021.
fig, ax = plt.subplots(1,2)
jul = data[data['month']==7]
ax[0].scatter(jul['day'], jul['flow'], alpha=0.8,
            s=0.02*jul['flow'], c=jul['year'], cmap='magma')
ax[0].set(yscale='log', xlabel='Day_July', ylabel='Observed Flow (cfs)')
Dec = data[data['month']==12]
ax[1].scatter(Dec['day'], Dec['flow'], alpha=0.8,
            s=0.02*Dec['flow'], c=Dec['year'], cmap='magma')
ax[1].set(yscale='log', xlabel='Day_December')
plt.show()

#6. Histograms for flow from July 1-15 and July 16-31

fig, ax = plt.subplots(1,2)
m = 10
mon_data = data[(data['month'] == m) & (data['day'] >= 1) & (data['day'] <= 15)]
ax[0].hist(np.log10(mon_data['flow']), bins=50, color='indigo')
ax[0].set(xlim=[1.75, 2.75], xlabel='Log_Observed_Flow cfs', ylabel='total', title='Flow for July 1st Half')

mon_data = data[(data['month'] == m) & (data['day'] >= 16) & (data['day'] <= 31)]
ax[1].hist(np.log10(mon_data['flow']), bins=30,
           color='red')
ax[1].set(xlabel='Log_Observed_Flow (cfs)', title='Flow for July 2nd Half')
plt.show()

# %%
