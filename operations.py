import numpy as np
from signals import *
from matplotlib import pyplot as plt
 

def sweep_match(x, rate = 0.1, amount = 1, r = 100):
    s, _ = chirp(x, kf = 1)
    h = []
    i = 0
    pslr_vector = []
    resol_vector = []
    kf_vector = []
    while True:
        h, _ = chirp(x, kf = 1 + i*rate)
        y = convolute(s, h)

        y_length = len(y)
        L = y_length
        pslr, mainlobe, sidelobe = PSLR(y, y_length)
        
        t = np.arange(-y_length/(2*r), y_length/(2*r), 1/r)
        i = i + 1
        res, x2, x1, z1, z2 = resolution(y,t, y_length/25)
        if amount <= 10:
            plt.plot(t, y, label = f"Kf = {1 + i*rate}")
            plt.hlines(mainlobe, -y_length/(2*r), y_length/(2*r), colors = "r", linestyles = "dashed")
            plt.hlines(sidelobe, -y_length/(2*r), y_length/(2*r), colors = "r", linestyles = "dashed")
            print(f"==================\n Curve {i}:\n PSLR (dB): {20*np.log10(sidelobe/mainlobe)}.\nResolution: {2*(t[x2] - t[x1])/(t[z1] - t[z2])}, {x1} e {x2}\n==================")
        pslr_vector.append(20*np.log10(sidelobe/mainlobe))
        resol_vector.append(2*(t[x2] - t[x1])/(t[z1] - t[z2]))
        kf_vector.append(1 + i*rate)
        if i == amount:
            print(f"chegou, i = {i}, amount = {amount}")
            plt.grid(True)
            plt.legend()
            plt.show()
            plot_performance(kf_vector, pslr_vector, resol_vector)
            break
    return (pslr_vector, resol_vector)

def convolute(s, h):
    y = np.convolve(s, h)
    length = len(y)
    return y/length
 

def convolution(s, h):

    y = []
    # See the convolution in the scratches.txt to understand this.
    limit_length = (len(s) + len(h) - 1)  # See "scratches"
    #print(f"Comprimentos Iniciais: {len(s)},  {len(h)},  {limit_length} ")
    s0s = len(h) - 1
    h0s = len(s) - 1
    zeroes_s = np.full(shape= s0s, fill_value= 0)
    s = np.insert(s, 0 , zeroes_s)
    zeroes_h = np.full(shape=h0s, fill_value=0)
    h = np.append(h, zeroes_h)
    while True:
        if len(y) == limit_length:
            #print(f"Convolução: {y}.")
            y = np.array(y)
            y = (1/limit_length)*y
            break
        #print(s)
        #print(h)
        conv = 0
        # Line of Convolution
        for k, v in enumerate(s):
            conv += h[k]*s[k]
        # Now add at the beg and the end
        s = np.append(s, 0)
        h = np.insert(h, 0, 0)
        #print(conv)
        y.append(conv)
        # Append the convolution as a signal number.
    return y

def PSLR(s, L):
    central_strip = int(L/2)
    max1 = s[0]
    max2 = s[0]

    for k, v in enumerate(s):
        if k < len(s) - 1:
            if k > len(s)/2 - central_strip and k < len(s)/2 + central_strip:
                 if v > max1 and v > s[k+1]:
                    max2 = max1
                    max1 = v


    if max2 != 0:
        PSLR_Value = max1/max2
    else:
        PSLR_Value = 0
    return (PSLR_Value,max1, max2)


def resolution(s, t,  L):
    const = 0.7071
    x1 = x2 = 0
    z1 = z2 = 0
    firstZero = False
    length = len(s)
    _, mlobe, slobe = PSLR(s, L)

    for k, v in enumerate(s):
        if k > (length - L)/2 and k < (length + L)/2:
            if v < const*mlobe and s[k+1] > const*mlobe:
                x1 = k + 1
            if v > const*mlobe and s[k+1] < const*mlobe:
                x2 = k
            if v > 0 and s[k+1] < 0 and  not firstZero:
                z1 = k
                if t[z1] > 0:
                    firstZero = True

            if v < 0 and s[k+1] > 0 and not firstZero:
                z2 = k


    return 2*(x2 - x1), x2, x1, z1, z2

def chirp_compression():
    pass


def plot_performance(kf, pv, rv):
    plt.plot(kf, pv, label="PSLR")
    plt.xlabel("Chirp Rate Ratio")
    plt.ylabel("Value")
    plt.title("Change in PSLR")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.plot(kf, rv, label="Resolution")
    plt.xlabel("Chirp Rate Ratio")
    plt.ylabel("Resolution")
    plt.title("Change in Resolution")
    plt.legend()
    plt.grid(True)
    plt.show()
 


'''L = 5
r = 200
x = np.arange(-L, L, 1/r)
sweep_match(x, -0.005, 3)'''