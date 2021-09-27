# Week 5: Python skills week 3<!-- omit in toc -->
This week we will be expanding our python skills focusing on Pandas DataFrames
____
## Table of Contents: <!-- omit in toc -->
- [To Do List](#to-do-list)
- [References](#references)
- [Training:](#training)
  - [1. Required Training Activities](#1-required-training-activities)
  - [2. Additional Optional Training Activities](#2-additional-optional-training-activities)
- [Assignment 5: Pandas DataFrames](#assignment-5-pandas-dataframes)
  - [Rules for this week:](#rules-for-this-week)
  - [Submission instructions:](#submission-instructions)
  - [Assignment questions](#assignment-questions)
- [Cheat Sheet Assignment 2: Python basics](#cheat-sheet-assignment-2-python-basics)
  - [Notes on Cheat Sheet formatting](#notes-on-cheat-sheet-formatting)
___
## To Do List
1. Complete the required training Activities by **next Tuesday**, get through as much as you can before class **Thursday**. Once again there is a lot of content this week so if you can start early  thats a good idea.
2. Submit your fifth streamflow forecast and assignment by **noon on Monday** following the instructions in the [ Forecast Assignment](#assignment-5-pandas-dataframes).
3. Submit your second [cheat sheet assignment](#cheat-sheet-assignment2-python-basics) by **midnight on Wednesday**

___
## References
- There is a *pandas-cheat-sheet.pdf* in the Cheet_sheets folder  that covers the major functions
- [Python Data Science Handbook Chapter 2](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html) (sections of this chapter are also assigned in the required training).
___
## Training:
### 1. Required Training Activities
Work through Chapter 15 of Intro to Earth Data Science covering Pandas DataFrames. Don't worry to much about the plotting included in these lessons we will get to this in mor detail next week. 
   - **Lesson 1**: [Pandas DataFrames Intro](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/)
   - **Lesson 2**: [Importing Data into DataFrames](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/import-csv-files-pandas-dataframes/) (NOTE: you can see in this exercise that the approach is the same that I have applied for the starter codes. You can use the example dataset they provide or just use the ones we have downloaded for homework already)
   - **Lesson 3**: [Recalculate and Summarize](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/run-calculations-summary-statistics-pandas-dataframes/) (Note: Same as the previous section you can do these exercises with they data they recommend or practice applying the same functions to the data you already have)
   - **Lesson 4**: [Selecting Data from DataFrames ](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/indexing-filtering-data-pandas-dataframes/) *This lesson is longer but very  important, make sure you walk through all of this.

### 2. Additional Optional Training Activities
Read the following sections from the [Python Data Science Handbook Chapter 3](ttps://jakevdp.github.io/PythonDataScienceHandbook/index.html). Note that this material is more detailed than the Earth Data Science Handbook. Its fine if you don't have time to work through every example they discuss but at a minimum you should read through these sections to be familiar with the concepts and know where to refer back to as needed:
   - [Introducing Pandas Objects](https://jakevdp.github.io/PythonDataScienceHandbook/03.01-introducing-pandas-objects.html)
   - [Data Indexing and Selection](https://jakevdp.github.io/PythonDataScienceHandbook/03.02-data-indexing-and-selection.html)
   - [Operating on Data in Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.03-operations-in-pandas.html)
   - [Handling Missing Data](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html)

___
## Assignment 5: Pandas DataFrames
We are still in the exploratory data phase. This week you will be using Pandas to look  at the historical streamflow and make your forecast. You should write a script to subset the data however is most useful to you for your decision making. The HW5 starter code will help you get your DataFrame setup and after that it is up to you.

(*Remember* you should copy the starter code into your own repo and not work with it directly on the course materials repo).

### Rules for this week:
- You must use the pandas dataframe *data* created at the top of the starter code as the basis for your analysis (i.e. don't use lists or numpy arrays, take advantage of all of the handy pandas functionality!)

- You can do any mathematical operation you would like on the dataset as long as you only use the numpy or pandas package to do so.  

- The only dataset you can use is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

### Submission instructions:
This week you should submit the following:

1. Your streamflow forecast values in the forecast repo in the csv with your name

2. Your assignment summary (see instructions below). This should be named with the same convention  as always 'lastname_HWx.md' and saved in the submission folder of your homework repo.  It should include
  1. An appropriate header,
  2. A summary of your forecast and how you made it
  3. Answers to all of the questions listed below

3. The python script you wrote to do your homework.  Just copy this script into the submission folder with the name 'lastname_HWx.py'

**NOTE**: If you woudl like to insert images into your markdown files I recommend you install the `Markdown Image` app.  To do the go to the `Extensions` botton on the left panel or under the View Menu and search for `Markdown Image` (see the picture below for what it looks like) and click install. You may need to restart vs-code for the app to start working. 
![picture 1](../../images/6df9e57f09c9cbc4af896046260514094567ec9fb0be64331b089a9b18b4c2ed.png)  


### Assignment questions
In addition to providing a summary of the forecast values you picked and why include the following analysis in your homework submission. Note that you could answer some of these questions using lists or numpy arrays, however this time you are expected to calculate your answer using the pandas dataframe *data* created in the starter code.

1. Provide a summary of the data frames properties.
  - What are the column names?
  - What is its index?
  - What data types do each of the columns have?

2. Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.

3. Provide the same information but on a monthly basis. 
   - HINT: You should use the `groupby` method to do this combined withe the `describe` method. You should not need a for loop. See [this link](https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/) for an example of how groupby works.

4. Provide a table with the 5 highest and 5 lowest flow
values for  the period of record. Include the date, month and flow values in your summary.
  - HINT: I would reccomnd using the `sort_values` and `head` and `tail` methods here. 

5.  Find the highest and lowest flow  values for every month of the year (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.
   - HINT: There are multiple ways to do this but one approach would be the following. 
     - Initialize some 1D arrays to stor your max and min values
     - Loop over the months 
       - For each month grab out just the flow values of that month
       - Sort them ascending by flow
       - Grab the year for the first value and save it in your min array
       - Grab the year for the last value and save that in your max array 

6. Provide a list of historical dates with flows that are within 10% of your week 1 forecast value. If there are none than increase the %10 window until you have at least one other  value and report the date and the new window you used
   - HINT: You should be able to do this on one line using conditionals

___
## Cheat Sheet Assignment 2: Python basics
1. Create a cheet sheet on Python basics that covers the following: 
   - Define: Packages, objects, functions, methods and atributes
   - Lists: What are they, how do you make them, what are some important methods to remember.
   - Indexing: Summarize how indexing and slicing works for lists and give examples of the different ways to access things (or 1D arrays)
   - Conditional statements:  Whats the syntax examples of different types of conditionals and conditional nesting. 
   - For Loops: What are these for and what's the syntax
   - List comprehensions  What are these and what's the syntax
2. Submit your cheat sheet to me in the `cheat_sheets` folder of your `homework-githubname` repo. Name your file `lastname_CS2_PythonBasics`

### Notes on Cheat Sheet formatting
- Reminder: it is entirely up to you though what your cheet sheet should look like, and note that you already have the ones provided in the content folder you so it doesn't need to be a duplicate of that. The point is for you to have a concise guide in your own words that will be helpful to you and that you can refer back to.
- This might take the form of a word document, a powerpoint slide, or even a hand written or drawn diagram, a jupyter notebook or pythhon script (when we get to those) or something more creative that I'm not thinking of yet :)
- In general I'm looking for something the equivalent of 1-2 pages long.
- All Cheat Sheet assignments will be graded pass/fail. If I determine yours needs work you will be able to resubmit the following Tuesday with a revised version.
