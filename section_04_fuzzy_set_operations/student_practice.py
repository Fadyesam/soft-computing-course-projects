"""Practice exercise for Section 4 fuzzy-set operations.

Students can first solve the formulas by hand, then run this script to check
and discuss the results.
"""

import numpy as np

from fuzzy_operations import (
    fuzzy_algebraic_product,
    fuzzy_intersection_min,
    fuzzy_union_max,
)


set_a = np.array([0.2, 0.6, 0.9, 0.4])
set_b = np.array([0.5, 0.3, 0.8, 0.1])

# Practice 1: Standard Union uses the element-by-element MAX operator.
union_result = fuzzy_union_max(set_a, set_b)

# Practice 2: Standard Intersection uses the element-by-element MIN operator.
intersection_result = fuzzy_intersection_min(set_a, set_b)

# Practice 3: Algebraic Product multiplies matching membership degrees.
product_result = fuzzy_algebraic_product(set_a, set_b)

# Practice 4: Verify the important inequality product <= MIN intersection.
comparison = product_result <= intersection_result

print("A:", set_a)
print("B:", set_b)
print("Union (MAX):", union_result)
print("Intersection (MIN):", intersection_result)
print("Algebraic Product:", product_result)
print("Product <= Intersection:", comparison)
print("True for every element:", bool(np.all(comparison)))
