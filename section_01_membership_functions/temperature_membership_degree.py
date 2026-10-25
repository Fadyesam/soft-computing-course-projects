"""Evaluate the membership degree of one crisp temperature.

The example shows how a single crisp value can partially belong to several
fuzzy sets at the same time.
"""

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz


# Universe of discourse with a small step for smooth curves.
temperature = np.arange(0, 50.1, 0.1)

# Membership functions for the linguistic terms Cold, Warm, and Hot.
cold = fuzz.trapmf(temperature, [0, 0, 10, 25])
warm = fuzz.trimf(temperature, [15, 25, 35])
hot = fuzz.trapmf(temperature, [25, 40, 50, 50])

# Crisp input to be fuzzified.
crisp_temperature = 10

# interp_membership finds the membership value at the crisp input by
# interpolation on the already-computed membership curve.
mu_cold = fuzz.interp_membership(temperature, cold, crisp_temperature)
mu_warm = fuzz.interp_membership(temperature, warm, crisp_temperature)
mu_hot = fuzz.interp_membership(temperature, hot, crisp_temperature)

print(f"Temperature = {crisp_temperature} °C")
print(f"Cold membership = {mu_cold:.2f}")
print(f"Warm membership = {mu_warm:.2f}")
print(f"Hot membership  = {mu_hot:.2f}")


plt.figure(figsize=(8, 5))
plt.plot(temperature, cold, label="Cold")
plt.plot(temperature, warm, label="Warm")
plt.plot(temperature, hot, label="Hot")

# Mark the crisp temperature with a vertical reference line.
plt.axvline(
    x=crisp_temperature,
    linestyle="--",
    linewidth=1.5,
    label=f"T = {crisp_temperature} °C",
)

# Mark the three membership values at the same crisp input.
plt.scatter([crisp_temperature] * 3, [mu_cold, mu_warm, mu_hot], zorder=5)

# Horizontal helper lines make the membership degrees easier to read.
for membership in (mu_cold, mu_warm, mu_hot):
    plt.hlines(
        membership,
        xmin=temperature.min(),
        xmax=crisp_temperature,
        linestyles="dotted",
        alpha=0.7,
    )

plt.text(crisp_temperature + 0.5, mu_cold, f"Cold = {mu_cold:.2f}")
plt.text(crisp_temperature + 0.5, mu_warm, f"Warm = {mu_warm:.2f}")
plt.text(crisp_temperature + 0.5, mu_hot, f"Hot = {mu_hot:.2f}")

plt.xlabel("Temperature (°C)")
plt.ylabel("Degree of Membership")
plt.title("Fuzzification of a Crisp Temperature")
plt.ylim(-0.05, 1.05)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
