#Assignmnent_9
#By: Jason Schlottman 
#Week9: API Utilized to source data
#Course: HAS Tools: Tools for Data Handling and Analysis in Water, Weather, & Climate
#Date: 10/19/2021

# %%
# Code below imports necessary packages:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json 
import urllib.request as req
import urllib

#make sure to 'pip install sklearn" then "conda install scikit-learn" then 'import sklearn'.
import sklearn

# %%
# Create URL for the rest API here:
# Insert your token here
jtoken = '836132e4d0c04a1399c325e087905feb'

# This is the base url that will be the start our final url
base_url = "http://api.mesowest.net/v2/stations/timeseries"

# Specific arguments for the data that we want
args = {
    'start': '199701010000',
    'end': '202009300000',
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
    'token': jtoken} 

# Take arguments and paste them together
apiString = urllib.parse.urlencode(args)
print(apiString)

# API string added to base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# API response:
response = req.urlopen(fullUrl)

# Next read data:
responseDict = json.loads(response.read())

# Rad data into Pandas dataframe:
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

# Now we can combine this into a pandas dataframe
data = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))

# Now convert this to daily data using resample
data_daily = data.resample('D').mean()

median_flow = data[data_daily]

Plot_1
# %%
