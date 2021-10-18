# Assignment_7: Code_Review
#Created by Jason Schlottman, utilizes functions and examples similar to those provided in past course assignment codes.
#Date: 10/08/2021

# > Although this .py file provides pseudocode, directions are found in "CodeReview1" directory located in the 'Forecast_Submissions' folder of the 'hw-jschlottman2' repo im the main GitHub course shared repository!
# As stated in the 'ReadMe' directions answers to the prompt for 'calculations', 'plots', & forecasts are returned by running their respective sections of code below:

# %%
" **Section_1** "

# Import the necesary python packages/modules.
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# %%
" **Section_2** "
# Define the correct path & filename to call in the streamflow discharge data.

filename = 'streamflow_week7.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

#filepath='../data/streamflow_week7.txt'

data = pd.read_table(filepath, sep = '\t', skiprows=30,
        names =['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)


# %%
" **Section_3** "
#Run conditonal staatements and built-in operations to calculate quantitave analysis of streamflow data.

print('The following data table dsiplays the calculations for the flow data:')

data["flow"].describe()

# %%
" **Section_4** "
# Run the code below to produce 3 seperate and unique plots to gain visual insight into how the streamflow varies over time.

#Plot_1: Time-Series LinePlot: Observed Daily Flow from 2010 to 2020
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], color='orange')
ax.set(title="A Decade of Observed Flow", xlabel="Date", 
        ylabel="Daily Average Flow [cfs]", yscale='log',
        xlim=[datetime.date(2010, 1, 1),
        datetime.date(2020, 12, 21)])
plt.show()

#Plot 2: Histogram Subplots:
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

#Plot_3: Scatter plot for flow in month of 07 & 12 for events from 1990-2021.
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

# %%
" **Section_5** "
# Run the following code to produce the 1-week and 2-week streamflow forecast estimates for the streamflow data.

f_1wk=npmean.flow()

f_2wk=npmean.flow()*0.8 

def forecast(f_1wk,f_2wk):
'''
Parameters:
f_1wk= estimated 1-week forecast value.
f_2wk= estimated 2-week forecast value.

Returns: Running this function returns two seperate integers which represent the 1-week and 2-week streamflow estimate values in cfs.

'''
        print(f_1wk)
        print(f_2wk)
# %%