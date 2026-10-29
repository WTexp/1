
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

# Triangular: Lightly Soiled
light = np.maximum(0, np.minimum(x/2, (4-x)/2))

# Trapezoidal: Moderately Soiled
moderate = np.maximum(0, np.minimum.reduce([
    (x-2)/2, np.ones(len(x)), (8-x)/2
]))

# Gaussian: Heavily Soiled
heavy = np.exp(-((x-9)**2)/(2*1.5**2))

plt.plot(x, light, label="Lightly Soiled")
plt.plot(x, moderate, label="Moderately Soiled")
plt.plot(x, heavy, label="Heavily Soiled")

plt.xlabel("Soil Level")
plt.ylabel("Membership Value")
plt.title("Washing Machine Fuzzy Membership Functions")
plt.legend()
plt.grid()
plt.show()
