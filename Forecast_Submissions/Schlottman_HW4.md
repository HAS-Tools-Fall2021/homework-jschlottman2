# **Assignment4_numpy_Arrays**
## **Jason Schlottman**
## Week 4 - 9/19/2021
## *Schlottman_HW4.md*
____________
## Grade
3/3 - Great job!  You are all caught up!!
Next time just make sure you preview your markdown formatting some of it didn't come through quite right. 
____________

### Assignment Summary:
#This week the basis for analyzing the streamflow data relies on utilizing data in the provided starter python code by using numpy arrayse edited to meet the conditions set in place with estimates returned using the numpy array to calculate the values and perform  operations in order to form my estimate for the 1 and 2-week streamflow forecast values representing this week's  predicted streamflow (cfs).

## Questions:
> 1. Provide a summary of the forecast values you picked and why. Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.

 #The forecast predictions were chosen based on a number of inputs to help estimate a reasonable flow in cfs. To start, we can observe the flow on a histogram and observe the mean and median flow, which helps provide an estimate of potential reasonable vakues that will fall within the range of true flow as it varies over the period. The mean value was over 400 cfs which is a little too large to be realistic in my opinion so i tended to favor the median estimate. The median flow rate was about 160 cfs when observing the flow for only the month of september in the year 2021 for all existing data. I scaled this down a bit for realism due to the end of the summer monsoons likely resulting in a decrease in flow over time eventually.  

> 2. Describe the variable flow_data:
  - What is it?
  - What type of values is is composed of?
  - What is are its dimensions, and total size?
#flow_data represents a numpy array consisting of the variables 'year','month','day', and 'flow'. This array is composed of a row for every day and 4 columns indicating year,month,day of the month, and flow value(cfs). The variables are represented by an index value of 0,1,2, or 3 and each can be edited to define a boundary condition. These object types are integers stored within a dat type known as an array.

> 3. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
#Total: 304 times
#Percentage: 304/975 = 31.18% exceedance

> 4. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
#In or before 2000:
#Total: 2526
#Percentage: 2526/4383 = 57.63% ocurrence of exceedance.  

#In or after 2010:
#Total: 1993
#Percentage: 1993/4276 = 46.61 % ocurrence of actual flow exceeding predicted flow.   
> 5. How does the daily flow generally change from the first half of September to the second?

#The first and second half of the month observe a postive trend with peak flow occuring towards the end of the month of september with values rising dramatically up to several thousand cfs in just a couple of weeks difference in time of flow.
