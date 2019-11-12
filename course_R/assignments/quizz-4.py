import numpy as np
from scipy.integrate import quad
def integrand(x):
    return 1./(np.sqrt(2. * np.pi)) * np.sin(x)**2.*np.exp(-x**2./2.)


I = quad(integrand, -10., 10.)
print(I)
