<<<<<<< HEAD
# **Assignment4_numpy_Arrays**
## **Jason Schlottman**
## Week 4 - 9/19/2021
## *Schlottman_HW4.md*

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
=======
#Assignment4_Week4_9/14/2021_Schlottman

*Schlottman_HW4.md*

## Grade
**1/3: This is a good start but it seems like you are missing most of the assignment here. I will give you until next Tuesday to re-submit. make sure to come to my office hours in advance next time if you have questions. 

- Your markdown formatting is not working because you are missing spaces after your formatting codes. Make sure you preview your markdown before submitting it. 
- for your summary I'm not really looking for a summary of what the assignment was asking you to do I'm asking for a summary of how you specifically picked your flow values. For example something like:  *I predict 90cf and 85cfs based on the fact that the long term average flows for september are xxx and I from my histogram analysis I have seen declining flows over the month of september etc etc...* Note that I ask in the instructions for at least two histograms and a discussion of flow quantiles in your answer
- For the rest of your answers in most cases you are missing the actual solution and just talking about how somthing might be done or not answering at all. 
_______

#Summary:
#This week the basis for analyzing the streamflow values relies on utilizing data in the provided python starter code focuses on attaining data from the numpy arrays rather than lists like we depended on previously. Now we can take advantage of defined arrays which allow for easier manipulation and conditional statements allow for easy calculations without having to write a ton of lists and extra code. Alongside conditional statements, we may use any type of mathematical operation as long as it is included in the provided numpy array called "*flow_data*" to calculate the necessary mathematical operations and form reasonable estimates for the 1-week and 2-week forecast values representing our estimates for the flow (cfs).

#Questions:

#1. Provide a summary of the forecast values you picked and why.  Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.

#2. Describe the variable "*flow_data*":
  -What is it?
#This variable is an object type known as an array which represents a return of an array of parameters, or any nested sequence.
  - What type of values is it composed of?
#The values composing the array can actually be formed by several types of variables. These can be any kind of variable such as integers, floats, or even boolean expressions! that fall under the array as they can be made as large or small as we choose to make them. In this array I believe the variables 'year', 'month','day' are all simply integers while 'flow' is a float.
 - What is are its dimensions, and total size?
# The dimensions of this array are found by using the function "numpy.flow_data : ndim". Then we can use a len() command to return the length of the variable which is returned from the first command. From this we see there are 

#3. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?

#4. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)

#5. How does the daily flow generally change from the first half of September to the second?
>>>>>>> master
