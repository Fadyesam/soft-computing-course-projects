"""Create triangular membership functions without an external fuzzy library."""

import matplotlib.pyplot as plt
import numpy as np


def triangular_membership(x, a: float, b: float, c: float) -> np.ndarray:
    """Return a triangular membership function with a < b < c.

    a: left foot of the triangle, where membership is 0
    b: peak of the triangle, where membership is 1
    c: right foot of the triangle, where membership returns to 0
    """
    if not a < b < c:
        raise ValueError("Triangular parameters must satisfy a < b < c.")

    x = np.asarray(x, dtype=float)

    # Rising edge: membership grows linearly from 0 to 1.
    rising = (x - a) / (b - a)

    # Falling edge: membership decreases linearly from 1 to 0.
    falling = (c - x) / (c - b)

    # The triangular membership is the smaller of the rising/falling lines,
    # clipped below at 0 so all values stay in the valid [0, 1] interval.
    return np.maximum(0, np.minimum(rising, falling))


if __name__ == "__main__":
    universe = np.linspace(0, 10, 500)

    # Same overlapping sets used in the section practical example.
    medium = triangular_membership(universe, 2, 5, 8)
    high = triangular_membership(universe, 5, 8, 10)

    print("Domain size:", len(universe))
    print("Maximum membership in Medium:", medium.max())
    print("Maximum membership in High:", high.max())

    plt.figure(figsize=(8, 5))
    plt.plot(universe, medium, label="A: Medium")
    plt.plot(universe, high, label="B: High")
    plt.xlabel("x")
    plt.ylabel("Membership Degree")
    plt.title("Triangular Membership Functions")
    plt.ylim(-0.05, 1.05)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
