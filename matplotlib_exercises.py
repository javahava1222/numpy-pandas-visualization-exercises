import matplotlib.pyplot as plt
import math

# 1) Use matplotlib to plot the following equation:

# y = x^2 − x + 2
# You'll need to write the code that generates the x and y points.

# Add an anotation for the point 0, 0, the origin
x = range(-10, 10)
y = [(n ** 2) - n + 2 for n in x]
plt.plot(x, y)
plt.text(0, 0, '(0, 0)', fontsize=10, color='blue')
plt.grid

# Create and label 4 separate charts for the following equations 
# (choose a range for x that makes sense):

# y=√x
x = range(-20, 20)
y = [math.sqrt(n) for n in x]
plt.plot(x, y)

# y=x^3
x = range(-10, 10)
i = [n ** 3 for n in x ]
plt.plot(x,i)

# y=2x
x = range(-10, 10)
j = [n * 2 for n in x]
plt.plot(x, j)

# y=1/(x+1)
x = range(-10, 10)
k = [(1/(n + 1)) for n in x]
plt.plot(x, k)

# You can use functions from the math module to help implement some of the equations above

#Combine the figures you created in the last step into one large figure with 4 subplots.
n_rows = 2
n_cols = 2

x = range(-30, 30)
y = [math.sqrt(n) for n in x]
i = [n ** 3 for n in x ]
j = [n * 2 for n in x]
k = [(1/(n + 1)) for n in x]


plt.subplot(n_rows, n_cols, 1)
plt.plot(x, y)
plt.title('y=√x')

plt.subplot(n_rows, n_cols, 2)
plt.plot(x, i)
plt.title('y=x^3')

plt.subplot(n_rows, n_cols, 1)
plt.plot(x, j)
plt.title('y=2x')

plt.subplot(n_rows, n_cols, 2)
plt.plot(x, k)
plt.title('$y=1/(x+1)$')

plt.show()

# Combine the figures you created in the last step into one figure 
# where each of the 4 equations has a different color for the points. 
# Be sure to include a legend and an appropriate title for the figure.