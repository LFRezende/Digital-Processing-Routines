import numpy as np
from signals import *
from operations import *
from matplotlib import pyplot as plt

L = 5
H = 50
r = 100
compression = 1
x = np.arange(-L, L, 1/r)
step = np.full(shape= L, fill_value= 1)
s, _ = chirp(x)
x = np.flip(x)
h, _ = chirp(x)
y = convolute(s, h)
y_length = len(y)
t = np.arange(-y_length/(2*r), y_length/(2*r), 1/r)
plt.plot(x, s, label="Signal")
'''plt.xlabel("Time")
plt.ylabel("Intensity")
plt.title("Signal")
plt.legend()
plt.grid(True)
plt.show()'''

plt.plot(t, y, label = "Convolution")
plt.xlabel("Time")
plt.ylabel("Intensity")
plt.title("Convoluted Signal")
plt.legend()
plt.grid(True)
plt.show()