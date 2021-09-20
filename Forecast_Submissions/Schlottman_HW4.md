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
