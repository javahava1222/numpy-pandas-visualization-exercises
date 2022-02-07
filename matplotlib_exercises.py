import matplotlib.pyplot as plt
import math

# 1) Use matplotlib to plot the following equation:

# y = x^2 − x + 2
# You'll need to write the code that generates the x and y points.

# Add an anotation for the point 0, 0, the origin
x = range(-100, 100)
y = [(n ** 2 - n + 2) for n in x]
plt.plot(x, y)
plt.title('$ y = x^2 - x +2$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.annotate('Origin', xy = (0,0), xytext = (0, 1000), arrowprops ={})
plt.grid
plt.plot

# Create and label 4 separate charts for the following equations 
# (choose a range for x that makes sense):

# y=√x
x1 = range(0, 100)
y1 = [n**(1/2) for n in x1]

plt.title('$ y = \sqrt{x}$')
plt.xlabel('$x$')
plt.ylabel('$\sqrt{x}$')
plt.xlim(0,100)
plt.ylim(0, 10)

plt.grid(True, ls = '--')
plt.plot(x1, y1)

# y=x^3
x2 = range(-20, 20)
y2 = [n ** 3 for n in x2 ]

plt.title('$ y = x^3$')
plt.xlabel('$x$')
plt.ylabel('$x^3$')
plt.xlim(-5,5)
plt.ylim(-40, 40)

plt.grid(True, ls = '--')
plt.plot(x2,y2)

# y=2^x
x3 = range(-10, 10)
y3 = [2**n for n in x3]
plt.title('$y = 2^x$')
plt.xlabel('$x$')
plt.ylabel('$2^x$')
plt.xlim(-5,5)
plt.ylim(0, 40)

plt.grid(True, ls = '--')
plt.plot(x3,y3)

# y=1/(x+1)
x4 = range(1, 10)
y4 = [1/(n + 1) for n in x4]
plt.title('$y = 1/(x+1)$')
plt.xlabel('$x$')
plt.ylabel('$1/(x+1)$')

plt.grid(True, ls = '--')
plt.plot(x4,y4)

# You can use functions from the math module to help implement some of the equations above

#Combine the figures you created in the last step into one large figure with 4 subplots.
plt.figure(figsize = (10,6))

#subplot 1
plt.subplot(221)

plt.title('$ y = \sqrt{x}$')
plt.xlabel('$x$')
plt.ylabel('$\sqrt{x}$')
plt.xlim(0,100)
plt.ylim(0, 10)

plt.grid(True, ls = '--')
plt.plot(x1, y1)

#subplot 2
plt.subplot(222)

plt.title('$ y = x^3$')
plt.xlabel('$x$')
plt.ylabel('$x^3$')
plt.xlim(-5,5)
plt.ylim(-40, 40)

plt.grid(True, ls = '--')
plt.plot(x2,y2)


#subplot 3
plt.subplot(223)

plt.title('$y = 2^x$')
plt.xlabel('$x$')
plt.ylabel('$2^x$')
plt.xlim(-5,5)
plt.ylim(0, 40)

plt.grid(True, ls = '--')
plt.plot(x3,y3)

#subplot 4
plt.subplot(224)

plt.title('$y = 1/(x+1)$')
plt.xlabel('$x$')
plt.ylabel('$1/(x+1)$')

plt.grid(True, ls = '--')
plt.plot(x4,y4)

plt.tight_layout()

# Combine the figures you created in the last step into one figure 
# where each of the 4 equations has a different color for the points. 
# Be sure to include a legend and an appropriate title for the figure.

plt.plot(x1, y1, c='pink', label='$\sqrt{x}$', alpha=.8)
plt.plot(x2, y2, c='burlywood', label='$x^{3}$', alpha=.8)
plt.plot(x3, y3, c= 'royalblue', label='$2^{x}$', alpha=.8)
plt.plot(x4, y4, c= 'firebrick', label='$1/(x+1)$', alpha=.8)

# adjust xlim and ylim
plt.ylim(0, 20)
plt.xlim(0, 20)

plt.ylabel('$y$')
plt.xlabel('$x$')
plt.title('Functions in One Graph')
plt.legend()

plt.show()