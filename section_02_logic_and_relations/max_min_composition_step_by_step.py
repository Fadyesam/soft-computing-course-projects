"""Compute fuzzy max-min composition step by step.

This version is intentionally verbose for classroom explanation.
"""

import numpy as np


r = np.array([
    [0.6, 0.9],
    [0.4, 0.7],
])

s = np.array([
    [0.8, 0.5],
    [0.3, 1.0],
])

if r.shape[1] != s.shape[0]:
    raise ValueError("Inner dimensions must match for max-min composition.")

rows = r.shape[0]
columns = s.shape[1]
intermediate_count = r.shape[1]

result = np.zeros((rows, columns), dtype=float)

# For each output cell T[i, j]:
# 1) Pair R[i, k] with S[k, j] for every intermediate index k.
# 2) Take MIN for each pair -> path strengths.
# 3) Take MAX of those path strengths -> final cell value.
for i in range(rows):
    for j in range(columns):
        path_strengths = []

        for k in range(intermediate_count):
            path_strength = min(r[i, k], s[k, j])
            path_strengths.append(path_strength)

            print(
                f"T[{i},{j}], k={k}: "
                f"min(R[{i},{k}]={r[i, k]:.1f}, "
                f"S[{k},{j}]={s[k, j]:.1f}) = {path_strength:.1f}"
            )

        result[i, j] = max(path_strengths)
        print(f"T[{i},{j}] = max{path_strengths} = {result[i, j]:.1f}\n")

print("Final max-min composition matrix:")
print(result)
