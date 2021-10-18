
# Instructions for running the revised version of the  'Code_Review' assignment are outlined in the text below:

## Refer to these directions to run the 'Schlottman_HW8.py' script while following along with the pseudocode to understand what each section returns. Follow directions and make sure to enter answer responses for the Prints, Plots, & Forecasts in the provided blank spaces after each italicized header entitled "### *AnswerX:* " ". Good luck!

'''
{
### Created by Jason Schlottman to provide directions for successfully running the 'Schlottman_HW8.py file found in the 'Forecast_Submissions' directory located within the 'homework-jschlottman2' repository found on the shared GitHub course repo 'HAS-Tools-Fall2021'.
}
'''

### **Outline of Code**

### Section 1: Run step_1 in the initial section to import python modules/packages.

### Section 2: Run step_2 to create the pandas_dataframe which calls all necessary variables

### Section 3: Run step_3 to return the "Prints" which display common calculations of the streamflow data which includes 'mean, median, std. deviation, quartiles' to gain a quantitative insight into actual streamflow conditions over time for the site.

### *AnswerPrints:* " "


### Section 4: The 'pandas_dataframe' - referenced variables are called in various conditional statements & functions to create 3 unique plots. (Ensure 'Markdown Image' for "VSCode" or 'markdown-image-assistant' for Atom text editors are installed in order to view plots!). These plots were chosen as a boxplot, a histogram, and a scatter plot. These choices deliver a number of visual representations of the flow data that helps the viewer gain a sense of insight into how trends occur and what shifts take place over time, both on an annual and daily scale, as well as how they compare to each other. By gaining a better understanding of the flow behavior, we can form better estimates and understand what determines a realistic forecast value.

### *AnswerPlots:* " "


### Section 5: After Running Section 1 through Section 4 you should use the returned plots and values to provide a 1-week and 2-week estimate for the streamflow in cubic feet per second. To do this Simply run Section 5 which will return the discharge values (in cfs).

### *AnswerForecasts:* " "


### Timeseries are an important part of the script in many parts of the function and plots. Notice how many lines of code reference the 'pandas_dataframe' data which references datetime. The plots and functions often call upon various periods and ranges of time whether through an indexed value of the date or time or through the resampling method. My script did not use the 'DateFormatter' command to change the desired format however this is a great way to increase code efficiency that I will be sure to attempt on future projects! We utilize these aids to help us easily code which allows us to provide insight into the data at any instantaneous moment or range of time. Whether we analyze the data on a specific day or time, weekly, monthly, or annually, doing so provides a sort of screenshot in time that allows us to look back and understand how the flow patterns shift and how the streamflow changes at that specific point in time. This is extremely useful and can be matched with known recorded events and attributed to sources such as large precipitation events or sudden discharge additions due to snowmelt in the warming months. All of these elements improve our understanding of the flow and allow us to form better predictions for future estimates.  

### **What I'm most proud of:** This script provides a variety of unique ways to analyze the data and returns both quantitative and qualitative results to help the reader understand what the changes in this data mean and what these shifts might indicate in the real-world. I can say I am most proud of developing plots as I feel the visual display of the data in these various formats really allows a deeper analysis on a level which all people can understand as visual results can be observed by anyone, not just atmospheric scientists or professionals who understand weather data simply by looking at values, especially in uncommon units that can be hard to visualize such as cubic feet per second.
