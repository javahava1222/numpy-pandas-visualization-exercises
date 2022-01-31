from http.client import _DataType
from pydataset import data
import pandas as pd
import numpy as np

# Copy the code from the lesson to create a dataframe full of student grades.
np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)
print(df)


# Create a column named passing_english that indicates whether each student
#  has a passing grade in english.
df['passing_english'] = english_grades > 70

# Sort the english grades by the passing_english column.
df.sort_values(by='passing_english', ascending = False)

#  How are duplicates handled? -- the duplicates are next to each other.

# Sort the english grades first by passing_english and then by student name. 
# All the students that are failing english should be first, 
# and within the students that are failing english they should be ordered alphabetically. 
# The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)
df.sort_values(['passing_english', 'name'], ascending = [True, True])

# Sort the english grades first by passing_english,
#  and then by the actual english grade, similar to how we did in the last step.
df.sort_values(['passing_english', 'english'], ascending = [True, True])

# Calculate each students overall grade and add it as a column on the dataframe. 
# The overall grade is the average of the math, english, and reading grades.
df['average'] = (df['math'] + df['english'] + df['reading']) / 3
print(df)

# Load the mpg dataset. 
# Read the documentation for the dataset and use it for the following questions:

# data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable
mpg

# How many rows and columns are there? -- A data frame with 234 rows and 11 variables
# What are the data types of each column?
mpg.dtypes
# manufacturer     object
# model            object
# displ           float64
# year              int64
# cyl               int64
# trans            object
# drv              object
# cty               int64
# hwy               int64
# fl               object
# class            object
# dtype: object

# Summarize the dataframe with .info and .describe
mpg.info()
mpg.describe()
# Rename the cty column to city.
mpg.rename(columns={'cty': 'city'}, inplace = True)

# Rename the hwy column to highway.
mpg.rename(columns={'hwy': 'highway'}, inplace = True)

# Do any cars have better city mileage than highway mileage? -- False
(mpg.city > mpg.highway).any()
# Create a column named mileage_difference 
# this column should contain the difference between 
# highway and city mileage for each car.
mpg['mileage_difference'] = (mpg.highway - mpg.city)

# Which car (or cars) has the highest mileage difference?
largest_difference = mpg.mileage_difference.nlargest()
largest_difference
mpg[mpg.mileage_difference == 12]
# 2008 Honda Civic and 1999 Volkswagen New Beetle

# Which compact class car has the lowest highway mileage? The best? -- 220	volkswagen	jetta  1999
boole = mpg['class'] == 'compact'
compact = mpg[boole]
compact.nsmallest(1, 'highway', keep='all')


# Create a column named average_mileage that is the mean of the city and highway mileage.
mpg['average_mileage'] = (mpg.city + mpg.highway)/2

# Which dodge car has the best average mileage? The worst?
boole1 = mpg['manufacturer'] == 'dodge'
dodge = mpg[boole1]
dodge.nlargest(1, 'average_mileage', keep='all')
# best ave_mile is caravan with ave mile of 21.
dodge.nsmallest(1, 'average_mileage', keep='all')
# worst ave_mile are ram 1500, durango, and dakota pickup

# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mam = data('Mammals')
data('Mammals', show_doc = True)

# How many rows and columns are there?
mam.shape  #  -- 107 rows and 4 columns

# What are the data types?
mam.dtypes
# weight      float64
# speed       float64
# hoppers        bool
# specials       bool
# dtype: object

# Summarize the dataframe with .info and .describe
mam.info() # all non-nulls
mam.describe()
#           weight	    speed
# count	107.000000	107.000000
# mean	278.688178	46.208411
# std	839.608269	26.716778
# min	0.016000	1.600000
# 25%	1.700000	22.500000
# 50%	34.000000	48.000000
# 75%	142.500000	65.000000
# max	6000.000000	110.000000

# What is the the weight of the fastest animal?
mam.nlargest(1, 'speed', keep='all')

mam.sort_values(by='speed', ascending=False).head(n=1)

# What is the overal percentage of specials?

# # How many animals are hoppers that are above the median speed? 
median_speed = mam.speed.median()
boole2 = (mam.speed > median_speed) & (mam.hoppers == True)
boole2
mam[boole2]

# What percentage is this?