import numpy as np
import matplotlib.pyplot as plt



# Use an interactive backend
plt.switch_backend('TkAgg')  

n = 10000
x = np.linspace(0,10,n+1)
y = np.exp(-x /10) * np.sin(x)

plt.plot(x,y)
plt.show()