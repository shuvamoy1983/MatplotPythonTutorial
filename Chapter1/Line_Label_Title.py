import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

x1 = []
y1 = []
for i in range(4):
    x.append(i)
    y.append(np.sin(i))
    x1.append(i)
    y1.append(np.sin(i)/2)

###label is used to identify the graph details within plot.
plt.plot(x,y,label="First_Line")
plt.plot(x1,y1,label="Second_Line")
plt.xlabel('X-Axis_Val')
plt.ylabel('Y-Axis_Val')
plt.title("Simple Graph\nCheck It Out")
###legend is used to print all the label inside the graph
plt.legend()
plt.show()