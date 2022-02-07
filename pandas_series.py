# <!-- Exercises Part I
# Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# Use pandas to create a Series named fruits from the following list:

fruit_list = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", 
"tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


# Use Series attributes and methods to explore your fruits Series.

# Determine the number of elements in fruits. --17
fruit_list.size

# Output only the index from fruits. -- RangeIndex(start=0, stop=17, step=1)
fruit_list.index

# Output only the values from fruits.
fruit_list.values

# Confirm the data type of the values in fruits.
fruit_list.dtype

# Output only the first five values from fruits. 
fruit_list.head(5)
# Output the last three values. 
fruit_list.tail(3)
# Output two random values from fruits.
fruit_list.sample(2)

# Run the .describe() on fruits to see what information it returns
#  when called on a Series with string values.
fruit_list.describe()
#count       17
# unique      13
# top       kiwi
# freq         4
# dtype: object

# Run the code necessary to produce only the unique string values from fruits.
fruit_list.value_counts()

# Determine how many times each unique string value occurs in fruits.
fruit_list.value_counts()
# kiwi                4
# mango               2
# strawberry          1
# pineapple           1
# gala apple          1
# honeycrisp apple    1
# tomato              1
# watermelon          1
# honeydew            1
# blueberry           1
# blackberry          1
# gooseberry          1
# papaya              1

# Determine the string value that occurs most frequently in fruits.
# kiwi                4
# Determine the string value that occurs least frequently in fruits. --papaya - 1
# all that counts to 1 are least frequently occurred in fruits_list


# Exercises Part II
# Explore more attributes and methods while you continue to work with the fruits Series.

# Capitalize all the string values in fruits.
fruit_list.str.upper()
fruit_list.str.capitalize()

# Count the letter "a" in all the string values (use string vectorization). --14 letters
def count_a(arg):
    count = 0
    for x in arg:
        if x == 'a':
            count += 1
    return count

fruit_list.apply(count_a).sum()

fruit_list.str.count('a')

# Output the number of vowels in each and every string value.
fruit_list
def vowel_count(arg):
    count = 0
    for x in arg:
        if x in 'aeiou':
            count += 1
    return count

fruit_list.apply(vowel_count)

# Write the code to get the longest string value from fruits. -- honeycrisp apple
def letter_count(arg):
    count = 0
    for i in arg:
        count += 1
    return count

fruit_list.apply(letter_count)
fruit_list.apply(letter_count).nlargest(n=1)
# above code gives the index at which the longest string value is, but does not return the string value itself
max_len = fruit_list.str.len().max()
boole = fruit_list.str.len() == max_len
fruit_list[boole]

max(fruit_list, key = len)



# Write the code to get the string values with 5 or more letters in the name.
def letter_five_more(arg):
    count = 0
    for i in arg:
        count += 1
    if count >= 5:
        return True 
    else:
        return False
fruit_list[fruit_list.apply(letter_five_more)]
# alternative way by using str method and boolean
fruit_list[fruit_list.str.len() >= 5]



# Use the .apply method with a lambda function to find the fruit(s)
#  containing the letter "o" two or more times.
fruit_list[fruit_list.str.count('o') >= 2]

fruit_list.apply([lambda fruit: fruit.st])


# Write the code to get only the string values containing the substring "berry".
fruit_list[fruit_list.str.contains('berry')]
fruit_list.apply([lambda x: 'berry'.st])

# Write the code to get only the string values containing the substring "apple".
fruit_list[fruit_list.str.contains('apple')]


# Which string value contains the most vowels?
vowel_count1 = fruit_list.str.count('[aeiou]')
vowel_count1
vowel_max = fruit_list.str.count('[aeiou').max()
boolea = fruit_list.str.count() == vowel_max
fruit_list[boolea]

# Exercises Part III
# Use pandas to create a Series named letters from the following string. 
# The easiest way to make this string into a Pandas series is to use list 
# to convert each individual letter into a single string on a basic Python list.
string = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

letters = pd.Series(list(string))
letters
#     'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
# Which letter occurs the most frequently in the letters Series?
letters.value_counts().sort_values(ascending=False)

# Which letter occurs the Least frequently?
letters.value_counts().nsmallest(n=1, keep='all')

# How many vowels are in the Series?
letters.str.lower().str.count('[aeiou]')
letters.str.lower().str.count('[aeiou]').sum()

# How many consonants are in the Series?
letters.str.lower().str.count('[^aeiou]').sum()

# Create a Series that has all of the same letters but uppercased.
letters.str.upper()

# Create a bar plot of the frequencies of the 6 most commonly occuring letters.

top7 = letters.value_counts().head(7)
top7.plot(kind='barh',
        width=.6)

plt.title('Top 6 Letters')

plt.gca().invert_yaxis()

plt.show()

# Use pandas to create a Series named numbers from the following list:

nums_list = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
numbers = pd.Series(nums_list)
numbers
#     ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
# What is the data type of the numbers Series?
numbers.dtype
# How many elements are in the number Series?
numbers.size
# Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
num_series = numbers.str.replace('$', '').str.replace(',','').astype('float')
# Run the code to discover the maximum value from the Series.
numbers.describe()
num_series.describe()
num_series.max()
# Run the code to discover the minimum value from the Series.
num_series.min()
# What is the range of the values in the Series?
num_series.max() - num_series.min()
# Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
num_series.value_counts(bins=4)
# Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
num_series.value_counts(bins=4).sort_index(ascending=False).plot(kind='barh', width=0.7)

plt.title('4 Bins')
plt.xlabel('Count')
plt.ylabel('$')
plt.show()
# Use pandas to create a Series named exam_scores from the following list:
scores_list = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores = pd.Series(scores_list)
#     [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
# How many elements are in the exam_scores Series?
exam_scores.size

# Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
exam_scores.describe()

# Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
exam_scores.plot.hist(width = 3)

plt.title('Exam Scores Distribution')
plt.xlabel('Scores')
plt.show()
# Write the code necessary to implement a curve for your exam_grades Series
#  and save this as curved_grades. 
# Add the necessary points to the highest grade to make it 100, 
# and add the same number of points to every other score in the Series as well.
curve = 100 - exam_scores.max()
curve
curved_grades = exam_scores + curve
curved_grades
# Use a method to convert each of the numeric values in the curved_grades Series 
# into a categorical value of letter grades. 
# For example, 86 should be a 'B' and 95 should be an 'A'. 
# Save this as a Series named letter_grades.
bin_edges = [0, 70, 75, 80, 90, 101]
bin_labels = ['F', 'D', 'C', 'B', 'A']

letter_grades = pd.cut(curved_grades, bins=bin_edges, labels=bin_labels)
letter_grades

letter_grades.value_counts().sort_index().plot.barh(color='royalblue',
                                                    ec='pink',
                                                    width=.8)

plt.title('Letter Grades')
plt.xlabel('Number of Students')
plt.ylabel('Letter Grade')

plt.show()

# Plot your new categorical letter_grades Series in a meaninful way 
# and include a title and axis labels.
bin_edges = [0, 70, 75, 80, 90, 101]
bin_labels = ['F', 'D', 'C', 'B', 'A']

plt.subplot(2,1,1)

pd.cut(exam_scores, 
       bins=bin_edges, 
       labels=bin_labels).value_counts().sort_index().plot.barh(color='red',
                                                                  ec='blue',
                                                                  width=.8)

plt.title('Letter Grades')
plt.xlabel('Number of Students')
plt.ylabel('Letter Grade')
plt.xlim(0, 8)

plt.show()

plt.subplot(2,1,2)
pd.cut(curved_grades,
         bins=bin_edges, 
         labels=bin_labels).value_counts().sort_index().plot.barh(color='royalblue',
                                                                                                ec='pink',
                                                                                                width=.8)
                
plt.title('Curved Letter Grades')
plt.xlabel('Number of Students')
plt.ylabel('Letter Grade')

plt.show()