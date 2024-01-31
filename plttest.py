import numpy as np
import matplotlib.pyplot as plt

#rndDataX = np.random.randint(100) --> Auxiliar func for integer generation

# (real numbers to simulate price)
rndDataX = np.random.random(500) * 120
rndDataY = np.random.random(500) * 120

#print(rndDataX)
color = "#0DABCD"

# Scatter chart --> standard distribution of values (that normaly do not hold a direct relation)
plt.scatter(rndDataX, rndDataY, c=color, marker="x", alpha=0.5)
plt.show()