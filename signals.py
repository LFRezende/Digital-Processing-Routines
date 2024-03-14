import numpy as np
PI = 3.1415926535897932384626433
def chirp(x, kf = 1, amp = 1, fcen = 0, compFactor=1):
    hr = amp*np.cos(PI*kf*compFactor*x**2 - 2*PI*fcen*x)
    hi = amp*np.sin(PI*kf*compFactor*x**2 - 2*PI*fcen*x)

    return hr, hi

def sinc(x, amp = 1,  compFactor = 1):
    h = amp*np.sin(PI*compFactor*x)/(PI*compFactor*x)
    return h