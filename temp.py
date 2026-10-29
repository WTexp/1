
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 40, 100)

# Triangular: Cold
cold = np.maximum(0, np.minimum((20-x)/10, (x-0)/10))

# Trapezoidal: Comfortable
comfortable = np.maximum(0, np.minimum.reduce([
    (x-10)/5, np.ones(len(x)), (30-x)/5
]))

# Gaussian: Hot
hot = np.exp(-((x-35)**2)/(2*5**2))

plt.plot(x, cold, label="Cold")
plt.plot(x, comfortable, label="Comfortable")
plt.plot(x, hot, label="Hot")

plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Value")
plt.title("Room Temperature Fuzzy Membership Functions")
plt.legend()
plt.grid()
plt.show()
