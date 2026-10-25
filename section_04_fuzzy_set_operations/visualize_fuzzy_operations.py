"""Visualize and compare fuzzy-set operations on continuous fuzzy sets."""

import matplotlib.pyplot as plt
import numpy as np

from fuzzy_operations import (
    fuzzy_algebraic_product,
    fuzzy_algebraic_sum,
    fuzzy_complement,
    fuzzy_intersection_min,
    fuzzy_union_max,
)
from triangular_membership_function import triangular_membership


universe = np.linspace(0, 10, 500)
set_a = triangular_membership(universe, 2, 5, 8)   # Medium
set_b = triangular_membership(universe, 5, 8, 10)  # High


plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(universe, set_a, label="Fuzzy Set A (Medium)")
plt.plot(universe, set_b, label="Fuzzy Set B (High)")
plt.title("Original Fuzzy Sets")
plt.xlabel("x")
plt.ylabel("Membership Degree")
plt.ylim(-0.05, 1.05)
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 2)
plt.plot(universe, set_a, "--", label="Set A")
plt.plot(universe, fuzzy_complement(set_a), label="Complement of A")
plt.title("Fuzzy Complement: 1 - A")
plt.xlabel("x")
plt.ylabel("Membership Degree")
plt.ylim(-0.05, 1.05)
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 3)
plt.plot(universe, fuzzy_union_max(set_a, set_b), label="MAX Union")
plt.plot(
    universe,
    fuzzy_algebraic_sum(set_a, set_b),
    "--",
    label="Algebraic Sum",
)
plt.title("Union Comparison")
plt.xlabel("x")
plt.ylabel("Membership Degree")
plt.ylim(-0.05, 1.05)
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 4)
plt.plot(
    universe,
    fuzzy_intersection_min(set_a, set_b),
    label="MIN Intersection",
)
plt.plot(
    universe,
    fuzzy_algebraic_product(set_a, set_b),
    "--",
    label="Algebraic Product",
)
plt.title("Intersection Comparison")
plt.xlabel("x")
plt.ylabel("Membership Degree")
plt.ylim(-0.05, 1.05)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
