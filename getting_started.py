"""
Importing Python modules

Modules (sometimes called packages or libraries) help group together related sets of tools in Python. In this exercise, we'll examine two modules that are frequently used by Data Scientists:

statsmodels: used in machine learning; usually aliased as sm
seaborn: a visualization library; usually aliased as sns
numpy: a module for performing mathematical operations on lists of data. 
"""

# tips:  Use * to represent the missing four letters

# plot

# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add a label to Mengfei's plot
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title("My Title")

# Add y-axis label
plt.ylabel('hours')

# Add a command to make the legend display
plt.legend()

# Display plot
plt.show()


# Adding a floating text
# Create plot
plt.plot(six_months.month, six_months.hours_worked)

# Add annotation "Missing June data" at (2.5, 80)
plt.text(2.5, 80, "Missing June data")

# Display graph
plt.show()


"""
Tracking crime statistics

Sergeant Laura wants to do some background research to help her better understand the cultural context for Bayes' kidnapping. 
She has plotted Burglary rates in three U.S. cities using data from the Uniform Crime Reporting Statistics.

https://www.ucrdatatool.gov/Search/Crime/Local/LocalCrimeLarge.cfm

She wants to present this data to her officers, and she wants the image to be as beautiful as possible to effectively tell her data story.

Recall:

You can change linestyle to dotted (':'), dashed('--'), or no line ('').
You can change the marker to circle ('o'), diamond('d'), or square ('s').
"""
# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle = ':')

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker = 's')

# Add a legend
plt.legend()

# Display the plot
plt.show()



"""
Playing with styles

Help Sergeant Laura wants to try out a few different style options. 
Changing the plotting style is a fast way to change the entire look of your plot without having to update individual colors or line styles. 
Some popular styles include:

'fivethirtyeight' - Based on the color scheme of the popular website
'grayscale' - Great for when you don't have a color printer!
'seaborn' - Based on another Python visualization library
'classic' - The default color scheme for Matplotlib
"""
# Choose any of the styles
plt.style.use("fivethirtyeight")

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()


# View all styles by typing print(plt.style.available) in the console
print(plt.style.available)

# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()





