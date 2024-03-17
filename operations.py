import numpy as np

def convolute(s, h):
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

'''def convolute2(s, h):
    y = []
    h = np.flip(h) #/(len(h)) # Normalize the filter.
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
        y.append((1/(max_length))*conv)
        if len(y) == max_length:
            break
    return y'''

    
    


def chirp_compression():
    pass
