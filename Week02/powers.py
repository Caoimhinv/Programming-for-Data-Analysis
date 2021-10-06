import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.0, 14.0, 0.1)

plt.plot(x, x**2, 'g.', label="x2")
plt.plot(x, x**3, 'b-', label="x3")
plt.plot(x, x**4, 'r-', label="x4")
plt.plot(x, 2**x, 'k-', label="2x")

plt.legend()

plt.show()