# **Assignment9_API_&Calling_Data_Alternatives**
## **Jason Schlottman**
## Week 9 - 10/25/2021
## *ReadMe_HW9.md*

### Assignment Summary:
This week's forecast vales rely on calling the data from a different source than previous weeks where the discharge values were simply downloaded from the USGS streamguage data provided online which could be downloaded as a '.txt.' file. For this assignment I have utilized an API to call in the streamflow data from an alternative site to the USGS database such as DayMet, or MesoNet's portal for a different site than usual, this time located at in Arizona where daily discharge in cfs is available for the station.

### The forecast values were determined by relying on the return from the Linear regression model and the output plot as well as using median streamflow returns as a backup to ensure values seemed to fall within reasonable range. By running both the linear regression model as well as a median streamflow return we form a nice comparison which allows us to gain insight into similarities and which method seems more consistent and reliable over time. Plu, this indicated which method seems more efficient for performing an analysis.

### The initial site i chose to analyze was sourced from the NOAA Station Mapper which was 'Walnut Creek', located near the Prescott National Forest at 34.930979, -112.807617. This site returned data for the period 01/01/2000-12/31/2010 and included the variabel precipitation (in). 

### Time series is extracted from the 'data' variable

### Plot  of Weekly Aggregated Values extracted from data which is a pandas_dataframe

### Returned forecast values defined by
