import numpy as np
import matplotlib.pyplot as plt

def normal_distribution(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

mu = 0
sigma = 1
x = np.linspace(-5, 5, 1000)
y = normal_distribution(x, mu, sigma)

plt.plot(x, y)
plt.show()
