import numpy as np
def convolute(s, h):
    y = []
    h = h #/(len(h)) # Normalize the filter.
    max_length = len(s) + len(h) - 1
    while True:
        m = 0
        conv = 0
        n = len(y)
        # Line of Convolution
        if n >= len(h):
            h = np.insert(h, 0, 0)  # To correct the size whilst not messing the correlation
        if n >= len(s):
            s = np.append(s, 0)
        while m <= n:
            conv += h[m]*s[m]
            m += 1
            
        # Append the convolution as a signal number.
        y.append(conv)
        if len(y) == max_length:
            break
    return y

    
    


def chirp_compression():
    pass