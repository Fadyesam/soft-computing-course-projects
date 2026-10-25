"""Reusable NumPy implementations of common fuzzy-set operations."""

import numpy as np


def _as_membership_array(values) -> np.ndarray:
    """Convert input to float array and validate membership degrees."""
    array = np.asarray(values, dtype=float)
    if np.any((array < 0) | (array > 1)):
        raise ValueError("Membership degrees must be in the interval [0, 1].")
    return array


def _validate_pair(mu1, mu2) -> tuple[np.ndarray, np.ndarray]:
    """Validate two membership arrays before a binary fuzzy operation."""
    first = _as_membership_array(mu1)
    second = _as_membership_array(mu2)
    if first.shape != second.shape:
        raise ValueError("Both fuzzy sets must have the same shape.")
    return first, second


def fuzzy_complement(mu) -> np.ndarray:
    """Standard complement: 1 - mu_A(x)."""
    membership = _as_membership_array(mu)
    return 1 - membership


def fuzzy_union_max(mu1, mu2) -> np.ndarray:
    """Standard union (s-norm): max(mu_A(x), mu_B(x))."""
    first, second = _validate_pair(mu1, mu2)
    return np.maximum(first, second)


def fuzzy_intersection_min(mu1, mu2) -> np.ndarray:
    """Standard intersection (t-norm): min(mu_A(x), mu_B(x))."""
    first, second = _validate_pair(mu1, mu2)
    return np.minimum(first, second)


def fuzzy_algebraic_product(mu1, mu2) -> np.ndarray:
    """Algebraic product: mu_A(x) * mu_B(x)."""
    first, second = _validate_pair(mu1, mu2)
    return first * second


def fuzzy_algebraic_sum(mu1, mu2) -> np.ndarray:
    """Algebraic sum: A + B - A*B."""
    first, second = _validate_pair(mu1, mu2)
    return first + second - (first * second)


def fuzzy_bounded_sum(mu1, mu2) -> np.ndarray:
    """Bounded sum: min(1, A + B)."""
    first, second = _validate_pair(mu1, mu2)
    return np.minimum(1, first + second)


def fuzzy_bounded_difference(mu1, mu2) -> np.ndarray:
    """Bounded difference: max(0, A - B)."""
    first, second = _validate_pair(mu1, mu2)
    return np.maximum(0, first - second)
