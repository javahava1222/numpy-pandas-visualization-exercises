#Excercise I

import pandas as pd
from env import get_db_url

query = '''
SELECT
    t.title as title,
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_no)
JOIN departments d USING (dept_no)
LIMIT 100
'''

title_dept = pd.read_sql(query, get_db_url('employees'))
title_dept.head()


# Once you have successfully run a query:

# a. Intentionally make a typo in the database url. 
# What kind of error message do you see? "Operational Error message"

# b. Intentionally make an error in your SQL query. 
# What does the error message look like? "Programming Error message"

# Read the employees and titles tables into two separate DataFrames.
sql = '''
SELECT *
FROM employees
'''

employees = pd.read_sql(sql, get_db_url('employees'))
employees

query = '''
SELECT *
FROM titles t
'''

titles = pd.read_sql(query, get_db_url('employees'))
titles


# How many rows and columns do you have in each DataFrame? 
# For employees table, 300024 rows by 6 columns
# For title table, 443308 rows by 4 columns
# Is that what you expected? Yes

# Display the summary statistics for each DataFrame.
employees.describe()
#       emp_no
# count	300024.000000
# mean	253321.763392
# std	161828.235540
# min	10001.000000
# 25%	85006.750000
# 50%	249987.500000
# 75%	424993.250000
# max	499999.000000
titles.describe()
# 	     emp_no
# count	443308.000000
# mean	253075.034430
# std	161853.292613
# min	10001.000000
# 25%	84855.750000
# 50%	249847.500000
# 75%	424891.250000
# max	499999.000000

# How many unique titles are in the titles DataFrame? -- 7 unique titles
titles.title.unique()
titles.title.describe()

# What is the oldest date in the to_date column? -- 1985-03-01
titles.to_date.sort_values().head(1)

# What is the most recent date in the to_date column? -- 9999-01-01
titles.to_date.sort_values().tail(1)

# Exercises II

# Copy the users and roles DataFrames from the examples above.
import numpy as np
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# What is the result of using a right join on the DataFrames?
users.merge(roles, left_on='role_id', right_on='id', how='right', indicator=True)
# right join returns all the key rows from the right table and matching rows from the left side.

# What is the result of using an outer join on the DataFrames?
users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)
#outer join is the union of two or more tables, which returns all the key data from the tables.

# What happens if you drop the foreign keys from the DataFrames and try to merge them?
users.merge(roles, left_on='role_id', right_on='id', how='left', indicator=True)

users.merge(roles, how='left', indicator=True)
#it performs the join operation without the right table's name which is connected to the foreign key's id.

# Load the mpg dataset from PyDataset.
from pydataset import data
mpg = data('mpg')

# Output and read the documentation for the mpg dataset.
data('mpg', show_doc = True)

# How many rows and columns are in the dataset?
# A data frame with 234 rows and 11 variables

# Check out your column names and perform any cleanup you may want on them.
mpg.drop(columns = ['drv', 'fl'])
mpg

# Display the summary statistics for the dataset.
mpg.describe()
# 	    displ	    year	    cyl	         cty	     hwy
# count	234.000000	234.000000	234.000000	234.000000	234.000000
# mean	3.471795	2003.500000	5.888889	16.858974	23.440171
# std	1.291959	4.509646	1.611534	4.255946	5.954643
# min	1.600000	1999.000000	4.000000	9.000000	12.000000
# 25%	2.400000	1999.000000	4.000000	14.000000	18.000000
# 50%	3.300000	2003.500000	6.000000	17.000000	24.000000
# 75%	4.600000	2008.000000	8.000000	19.000000	27.000000
# max	7.000000	2008.000000	8.000000	35.000000	44.000000

# How many different manufacturers are there? --15 manufacturers
mpg.groupby('manufacturer').describe()

# How many different models are there? -- 38 models
mpg.groupby('model').describe()

# Create a column named mileage_difference like you did in the DataFrames exercises; 
# this column should contain the difference between highway and city mileage for each car.
mpg['mileage_difference'] = mpg['hwy'] - mpg['cty']
mpg

# Create a column named average_mileage like you did in the DataFrames exercises; 
# this is the mean of the city and highway mileage.
mpg['average_mileage'] = (mpg['hwy'] + mpg['cty'])/2
mpg

# Create a new column on the mpg dataset named is_automatic 
# that holds boolean values denoting whether the car has an automatic transmission.
mpg['is_automatic'] = mpg['trans'].str.contains('auto')
mpg

# Using the mpg dataset, find out which which manufacturer has the 
# best miles per gallon on average? -- Honda
mpg.groupby('manufacturer').agg('mean').sort_values(by='average_mileage', ascending = False).head(1)

# Do automatic or manual cars have better miles per gallon? -- manual has better mpg on average
mpg.groupby('is_automatic').agg('mean').sort_values('average_mileage')

# Exercises III
# Use your get_db_url function to help you explore the data from the chipotle database.
query = '''
SELECT *
FROM orders
'''

chipotle_db = pd.read_sql(query, get_db_url('chipotle'))
chipotle_db

# What is the total price for each order?
chipotle_db['item_price'] = chipotle_db.item_price.str.replace('$', '').astype(float)
chipotle_db
chipotle_db.groupby('order_id').item_price.sum()

# What are the most popular 3 items?
chipotle_db.groupby('item_name').quantity.sum().sort_values(ascending = False).head(3)
# Chicken Bowl           761
# Chicken Burrito        591
# Chips and Guacamole    506

# Which item has produced the most revenue?
chipotle_db.groupby('item_name').item_price.sum().sort_values(ascending = False).head(1)
#Chicken Bowl    7342.73

# Join the employees and titles DataFrames together.
emp_titles = employees.merge(titles, on='emp_no')

# For each title, find the hire date of the employee
#  that was hired most recently with that title.
emp_titles.groupby('title').hire_date.max()
# Assistant Engineer    1999-12-24
# Engineer              2000-01-28
# Manager               1992-02-05
# Senior Engineer       2000-01-01
# Senior Staff          2000-01-13
# Staff                 2000-01-12
# Technique Leader      1999-12-31

# Write the code necessary to create a cross tabulation of the number of titles 
# by department. (Hint: this will involve a combination of SQL code 
# to pull the necessary data and python/pandas code to perform the manipulations.)
dept_title_query = '''

                    SELECT t.emp_no, 
                    t.title, 
                    t.from_date, 
                    t.to_date, 
                    d.dept_name 
                    FROM departments AS d 
                    JOIN dept_emp AS de USING(dept_no) 
                    JOIN titles AS t USING(emp_no);

                    '''
dept_titles = pd.read_sql(dept_title_query, get_db_url('employees'))
dept_titles.head()

titles_crosstab = pd.crosstab(dept_titles.dept_name, dept_titles.title)
titles_crosstab

#current employees
current_titles = dept_titles[dept_titles.to_date == dept_titles.to_date.max()]
current_titles.head()

current_titles_crosstab = pd.crosstab(current_titles.dept_name, current_titles.title)
current_titles_crosstab

# highlight max numbers in crosstab
current_titles_crosstab.style.highlight_max(axis=1)