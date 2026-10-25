"""Apply seven fuzzy-set operations to a discrete temperature example."""

import numpy as np

from fuzzy_operations import (
    fuzzy_algebraic_product,
    fuzzy_algebraic_sum,
    fuzzy_bounded_difference,
    fuzzy_bounded_sum,
    fuzzy_complement,
    fuzzy_intersection_min,
    fuzzy_union_max,
)


# Universe of discourse: candidate room temperatures in Celsius.
universe = np.array([15, 20, 25, 30])

# A = "Comfortable Temperature"
set_a = np.array([0.1, 0.8, 1.0, 0.3])

# B = "Warm Temperature"
set_b = np.array([0.0, 0.3, 0.7, 0.9])


def as_pairs(values: np.ndarray) -> list[tuple[int, float]]:
    """Represent membership values as readable (x, mu(x)) pairs."""
    return [
        (int(x_value), round(float(membership), 2))
        for x_value, membership in zip(universe, values)
    ]


results = {
    "Complement of A": fuzzy_complement(set_a),
    "Union A ∪ B (MAX)": fuzzy_union_max(set_a, set_b),
    "Intersection A ∩ B (MIN)": fuzzy_intersection_min(set_a, set_b),
    "Algebraic Product A · B": fuzzy_algebraic_product(set_a, set_b),
    "Algebraic Sum A + B": fuzzy_algebraic_sum(set_a, set_b),
    "Bounded Sum A ⊕ B": fuzzy_bounded_sum(set_a, set_b),
    "Bounded Difference A ⊖ B": fuzzy_bounded_difference(set_a, set_b),
}

print("Universe X:", universe.tolist())
print("A =", as_pairs(set_a))
print("B =", as_pairs(set_b))
print()

for name, values in results.items():
    print(f"{name:32s} = {as_pairs(values)}")


# Important comparison from the practical section:
# For membership degrees in [0, 1], A*B is never greater than min(A, B).
# Therefore, Algebraic Product is a stricter intersection than standard MIN.
min_intersection = fuzzy_intersection_min(set_a, set_b)
algebraic_product = fuzzy_algebraic_product(set_a, set_b)

print("\nCheck: Algebraic Product <= MIN Intersection")
for x_value, product_value, min_value in zip(
    universe,
    algebraic_product,
    min_intersection,
):
    print(
        f"x={x_value}: {product_value:.2f} <= {min_value:.2f} "
        f"-> {product_value <= min_value}"
    )
