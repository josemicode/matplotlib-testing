import numpy as np
import matplotlib.pyplot as plt

#prices = np.random.randint(50, 100, size=14) --> aux func for integer arrays

years = [2010 + x for x in range(14)]
prices = np.random.random(14) * 50 + 50

years2 = [2010 + x for x in range(14)]
prices2 = np.random.random(14) * 50 + 50

# plot charts --> linear representation, commonly used to show tendencies across time
plt.plot(years, prices, "b--", lw=2)
plt.plot(years2, prices2, "r-", lw=1)

plt.show()