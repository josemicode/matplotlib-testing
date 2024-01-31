import numpy as np
import matplotlib.pyplot as plt

#rndDataX = np.random.randint(100)

rndDataX = np.random.random(500) * 100
rndDataY = np.random.random(500) * 100

#print(rndDataX)
color = "#0DABCD"

plt.scatter(rndDataX, rndDataY, c=color, marker="x", alpha=0.5)
plt.show()