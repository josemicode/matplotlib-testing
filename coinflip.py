import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# This file is an example of how a graph can be animated with the function pause()

# It works by following a simple coinflip iterative structure where the array's index is selected randomly and the integer in said position is incremented by one, then the graph is updated and paused for a fraction of a second

style.use("dark_background")

headsTails = [0, 0]

for _ in range(1000):
	headsTails[np.random.randint(2)] += 1
	plt.bar(["Heads", "Tails"], headsTails, color = ["red", "yellow"])
	plt.pause(0.001)

plt.show()