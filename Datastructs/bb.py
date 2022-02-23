import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


storeans=[]
x = np.linspace(0, 8, 100)
print(x)
for i in x:
    storeans.append(min(0.1201452*(i**1.516158), 1))
#max(min(my_value, max_value), min_value)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x, storeans, 'r')

# show the plot
plt.show()