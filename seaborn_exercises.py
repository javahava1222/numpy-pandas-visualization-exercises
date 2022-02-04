# Use the iris database to answer the following quesitons:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from pydataset import data

iris = data('iris')
iris.dtypes

# What does the distribution of petal lengths look like?
sns.displot(iris['Petal.Length'])
plt.show()

# Is there a correlation between petal length and petal width?
sns.scatterplot()
iris.corr() 
# 0.962865 correlation btw petal length and petal width

# Would it be reasonable to predict species based on sepal width and sepal length? 
# For this, you'll visualize two numeric columns through the lense of a categorical column.
# Which features would be best used to predict species?
iris.catplot()

# Using the lesson as an example, 
# use seaborn's load_dataset function to load the anscombe data set. 
anscombe = sns.load_dataset('anscombe')
anscombe
# Use pandas to group the data by the dataset column, 
# and calculate summary statistics for each dataset. What do you notice?
anscombe.groupby('dataset').describe()

# Plot the x and y values from the anscombe data. 
# Each dataset should be in a separate column.
sns.relplot(x='x', y='y', data=anscombe, col = 'dataset')
plt.show
# Load the InsectSprays dataset and read it's documentation. 
# Create a boxplot that shows the effectiveness of the different insect sprays.

# Load the swiss dataset and read it's documentation. 
# The swiss dataset is available from pydatset rather than seaborn. 
# Create visualizations to answer the following questions:

# Create an attribute named is_catholic that holds a boolean value of 
# whether or not the province is Catholic. 
# (Choose a cutoff point for what constitutes catholic)
# Does whether or not a province is Catholic influence fertility?
# What measure correlates most strongly with fertility?
# Using the chipotle dataset from the previous exercise, 
# create a bar chart that shows the 4 most popular items and the revenue produced by each.

# Load the sleepstudy data and read it's documentation. 
# Use seaborn to create a line chart of all the individual subject's 
# reaction times and a more prominant line showing the average change in reaction time. -->