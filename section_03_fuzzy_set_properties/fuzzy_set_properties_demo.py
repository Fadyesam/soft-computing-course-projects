"""Demonstrate common properties of a discrete fuzzy set.

The example uses a simple single-peaked temperature fuzzy set and computes:
support, boundary, crossover points, core, bandwidth, alpha-cuts,
cardinality, relative cardinality, symmetry, convexity, and singleton status.
"""

import matplotlib.pyplot as plt
import numpy as np


# Universe of discourse and corresponding membership degrees.
x = np.array([20, 25, 30, 35, 40])
mu = np.array([0.0, 0.5, 1.0, 0.5, 0.0])

if len(x) != len(mu):
    raise ValueError("x and mu must have the same number of elements.")
if np.any((mu < 0) | (mu > 1)):
    raise ValueError("Membership degrees must be in the interval [0, 1].")


# Support: all elements whose membership is greater than zero.
support = x[mu > 0]

# Boundary: elements that partially belong to the fuzzy set (0 < mu < 1).
boundary = x[(mu > 0) & (mu < 1)]

# Crossover points: elements whose membership degree is exactly 0.5.
# np.isclose is safer than == for floating-point comparisons.
crossover_points = x[np.isclose(mu, 0.5)]

# Core: elements with full membership.
core = x[np.isclose(mu, 1.0)]

# For this discrete example, bandwidth is measured as the distance between
# the first and last support values.
bandwidth = support.max() - support.min() if support.size else 0

# Alpha-cut includes elements with mu >= alpha.
# Strong alpha-cut includes only elements with mu > alpha.
alpha = 0.5
alpha_cut = x[mu >= alpha]
strong_alpha_cut = x[mu > alpha]

# Sigma-count (fuzzy cardinality) is the sum of all membership degrees.
cardinality = np.sum(mu)
relative_cardinality = cardinality / len(x)


# Symmetry check around the peak of this discrete example.
center = x[np.argmax(mu)]
is_symmetric = True
for index, value in enumerate(x):
    reflected_value = 2 * center - value
    reflected_indices = np.where(x == reflected_value)[0]

    # If the reflected point is part of the universe, both membership values
    # should match. This is a classroom-oriented discrete symmetry check.
    if reflected_indices.size:
        reflected_index = reflected_indices[0]
        if not np.isclose(mu[index], mu[reflected_index]):
            is_symmetric = False
            break


# Simplified convexity test for an ordered, single-peaked discrete fuzzy set:
# memberships should be non-decreasing up to the peak and non-increasing
# after the peak. This matches the current teaching example.
peak_index = np.argmax(mu)
is_non_decreasing = np.all(np.diff(mu[: peak_index + 1]) >= 0)
is_non_increasing = np.all(np.diff(mu[peak_index:]) <= 0)
is_convex = is_non_decreasing and is_non_increasing

# A fuzzy singleton has exactly one element with non-zero membership.
is_fuzzy_singleton = np.sum(mu > 0) == 1


print("Support:", support)
print("Boundary:", boundary)
print("Crossover points:", crossover_points)
print("Core:", core)
print("Discrete bandwidth:", bandwidth)
print(f"Alpha-cut (alpha={alpha}):", alpha_cut)
print(f"Strong alpha-cut (alpha={alpha}):", strong_alpha_cut)
print("Cardinality:", cardinality)
print("Relative cardinality:", relative_cardinality)
print("Symmetric:", is_symmetric)
print("Convex:", is_convex)
print("Fuzzy singleton:", is_fuzzy_singleton)


plt.figure(figsize=(8, 5))
plt.plot(x, mu, marker="o", linewidth=2, label="Hot Temperature")
plt.axhline(alpha, linestyle="--", label=f"Alpha = {alpha}")
plt.scatter(
    crossover_points,
    np.full(crossover_points.size, alpha),
    zorder=5,
    label="Crossover Points",
)
plt.scatter(core, np.ones(core.size), s=90, zorder=5, label="Core")
plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Degree")
plt.title("Fuzzy Set Properties: Hot Temperature")
plt.ylim(-0.05, 1.1)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
