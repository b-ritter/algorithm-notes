import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 5., .1)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, 10*t*np.sin(t*np.pi))
plt.show()