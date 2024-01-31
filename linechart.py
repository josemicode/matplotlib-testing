import numpy as np
import matplotlib.pyplot as plt

#rndDataX = np.random.randint(100)

years = [2010 + x for x in range(14)]
prices = np.random.random(14) * 50 + 50
#prices = np.random.randint(50, 100, size=14)

plt.plot(years, prices, "b--", lw=2)

years = [2010 + x for x in range(14)]
prices = np.random.random(14) * 50 + 50

plt.plot(years, prices, "r-", lw=1)
plt.show()