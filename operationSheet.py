import numpy as np
from signals import *
from operations import *
from matplotlib import pyplot as plt

L = 20
H = 5
r = 500
checkSinc =  False
checkSweep = True

PSLR_v = 0
mainlobe = 0
sidelobe = 0
strip = 1*r



x = np.arange(-L, L, 1/r)
step = np.full(shape= 2*L*r, fill_value= 1)

if checkSweep:
    sweep_match(x, rate = 0.0001, amount = 200, r = r)
s, _ = chirp(x, kf = 1)
h, _ = chirp(x, kf = 1 )# Baixo descasamento (~0.5%) AUMENTA o PSLR!!!
y = convolute(s, h)

if checkSinc:
    y = sinc(x)

PSLR_v, mainlobe, sidelobe = PSLR(y, strip)

y_length = len(y)

t = np.arange(-y_length/(2*r), y_length/(2*r), 1/r)
res, x2, x1, z1, z2 = resolution(y,t,  strip)

print(f"======================\nPSLR dB: {20*np.log10(sidelobe/mainlobe)} dB\nPSLR: {PSLR_v}, {mainlobe} e {sidelobe}\nSize: {res}, {x1} e {x2}\n======================")
print(f"======================\nResolution: {2*(t[x2] - t[x1])/(t[z1] - t[z2])}, {x1} e {x2}\n======================")

 
#plt.plot(x, s, label="Signal")
plt.vlines(t[int(len(t)/2 - strip/2)], -1, 1, colors = "r", linestyles="dashed")
plt.vlines(t[int(len(t)/2 + strip/2)], -1, 1, colors = "r", linestyles="dashed")
plt.vlines(t[int(z2)], -1, 1, colors = "g", linestyles="dotted")
plt.vlines(t[int(z1)], -1, 1, colors = "g", linestyles="dotted")
plt.vlines(t[int(x1)], -1, 1, colors = "y", linestyles="dotted")
plt.vlines(t[int(x2)], -1, 1, colors = "y", linestyles="dotted")
plt.hlines(mainlobe, -L, L, colors = "r", linestyles = "dashed")
plt.hlines(sidelobe, -L, L, colors = "r", linestyles = "dashed")
plt.plot(t, y, label = "Convolution")
plt.xlabel("Time")
plt.ylabel("Intensity")
plt.title("Convoluted Signal")
plt.legend()
plt.grid(True)
plt.show()