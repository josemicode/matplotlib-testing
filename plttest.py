import numpy as np
import matplotlib.pyplot as plt

#rndDataX = np.random.randint(100)

# (real numbers simulate price)
rndDataX = np.random.random(500) * 120
rndDataY = np.random.random(500) * 120

#print(rndDataX)
color = "#0DABCD"

plt.scatter(rndDataX, rndDataY, c=color, marker="x", alpha=0.5)
plt.show()