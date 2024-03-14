import numpy as np
from signals import *
from matplotlib import pyplot as plt

L = 5
r = 100

compression = 2

x = np.arange(-L, L, 1/r)
y, _ = chirp(x, compFactor = compression)
plt.plot(x, y, label = "Chirp")
plt.xlabel("Time")
plt.ylabel("Intensity")
plt.title("Chirp Pulse")
plt.legend()
plt.grid(True)
plt.show()