# **Assignment3_Lists**
## Jason Schlottman
## Week3 - 9/07/2021
### *Schlottman_HW3.md*

____________
## Grade
3/3 - Great job! 
____________

### Assignment Summary:
 #To make reasonable forecast estimates I made changes to the provided .py starter code and simply changed elements within the for loop in order to impose conditions to meet the criteria of each question. I also utilized Conditional statements and functions such as the len() to measure values and boolean expressions to note the analysis period and flow intensity. This is how I formed estimates for my 1 and 2-week predictions for the forecasting of the stream discharge values in cubic feet per second (cfs).

### Assignment Questions:
> #1. Describe the variables flow, year, month, and day. What type of objects are they? What data types are they composed of? How long are they?

 #flow, year, month and day are variables within the list created in the starter code. All are known as the object type called "numbers" where flow is a float, and year, month, and day are integers. All have a length of 11,945 values. All have data types of list.

> #2. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?

#According to the python return after imposing the conditions by changing the variables within the for loop I found that the daily flow was greater than my prediction of 105 cfs exactly 561 times in the month of September.

#Total= 561

#Percentage= 561/974 = 57.6% occurence of actual flow exceeding predicted flow of 105cfs in September.

> #3. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)

The daily flow exceeded my predicted flow of 105 cfs precisely 3327 times before and during the year 2000.

#Total= 3327

#Percentage= 3327/4383 = 75.91% occurence of actual flow exceeding predicted flow in or before the year 2000.

> #If we consider only daily flows in or after 2010?

#Total= 2782

#Percentage= 2782/4275 = 65.07%

> #4. How does the daily flow generally change from the first half of September to the second?

#The daily flow shifts in a major upward trend when comparing the general flow pattern for the first and second halves of the month of September independently. The first half is composed of very small values ranging from a few hundred up to a few thousand. The second half is mainly composed of flows between 5000-11,000 cfs, which is much higher.
