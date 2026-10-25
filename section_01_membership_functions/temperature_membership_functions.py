"""Plot common fuzzy membership functions for a temperature variable.

This example introduces triangular, trapezoidal, and Gaussian membership
functions on the same universe of discourse.
"""

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz


# Universe of discourse: temperature values from 0 to 100 °C.
temperature = np.arange(0, 101, 1)

# A triangular membership function is defined by three points [a, b, c].
# Here, [0, 0, 50] creates a left-shoulder shape for the linguistic term "Cold".
cold = fuzz.trimf(temperature, [0, 0, 50])

# A trapezoidal membership function is defined by four points [a, b, c, d].
# Membership rises from a->b, stays 1 between b and c, then falls from c->d.
warm = fuzz.trapmf(temperature, [20, 40, 60, 80])

# A Gaussian membership function uses a center (mean) and spread (sigma).
# It creates a smooth bell-shaped curve around the center value.
hot = fuzz.gaussmf(temperature, 50, 15)


plt.figure(figsize=(8, 5))
plt.plot(temperature, cold, linewidth=1.5, label="Cold")
plt.plot(temperature, warm, linewidth=1.5, label="Warm")
plt.plot(temperature, hot, linewidth=1.5, label="Hot")
plt.title("Fuzzy Membership Functions for Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Degree of Membership")
plt.ylim(-0.05, 1.05)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
