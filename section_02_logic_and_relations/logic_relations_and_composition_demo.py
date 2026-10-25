"""Section 2 practical demos: logic, relations, and fuzzy composition.

Topics:
1. Boolean logic and De Morgan's laws.
2. Predicates and quantifiers using all()/any().
3. Cartesian products and crisp relations.
4. Crisp relation matrices.
5. Boolean relation composition.
6. Fuzzy max-min composition.
7. A small AI matching example.
"""

from itertools import product

import numpy as np


def demo_boolean_logic() -> None:
    """Show Boolean operators and verify both De Morgan laws."""
    print("\n=== 1) Boolean Logic + De Morgan's Laws ===")

    a, b = True, False
    print("A =", a, "B =", b)
    print("A AND B =", a and b)
    print("A OR B  =", a or b)
    print("NOT A   =", not a)

    # product([False, True], repeat=2) generates all four truth-table rows.
    # Each assert verifies that the left and right sides of De Morgan's laws
    # are identical for every possible Boolean input pair.
    for a, b in product([False, True], repeat=2):
        not_and = not (a and b)
        not_a_or_not_b = (not a) or (not b)

        not_or = not (a or b)
        not_a_and_not_b = (not a) and (not b)

        print(
            f"A={a:<5} B={b:<5} | "
            f"NOT(A AND B)={not_and:<5}  "
            f"NOT A OR NOT B={not_a_or_not_b:<5} | "
            f"NOT(A OR B)={not_or:<5}  "
            f"NOT A AND NOT B={not_a_and_not_b:<5}"
        )

        assert not_and == not_a_or_not_b
        assert not_or == not_a_and_not_b


def demo_predicates_and_quantifiers() -> None:
    """Represent universal/existential quantifiers using all() and any()."""
    print("\n=== 2) Predicates + Quantifiers ===")

    students = [
        {"name": "Ali", "studies_ai": True, "studies_ml": False, "grade": 88},
        {"name": "Mona", "studies_ai": True, "studies_ml": True, "grade": 95},
        {"name": "Omar", "studies_ai": True, "studies_ml": False, "grade": 76},
    ]

    # Universal quantifier (for all): every student studies AI.
    every_student_studies_ai = all(s["studies_ai"] for s in students)

    # Existential quantifier (there exists): at least one student studies ML.
    exists_ml_student = any(s["studies_ml"] for s in students)

    # NOT exists: no student has a grade greater than 100.
    no_grade_over_100 = not any(s["grade"] > 100 for s in students)

    print("Every student studies AI:", every_student_studies_ai)
    print("There exists an ML student:", exists_ml_student)
    print("No grade is over 100:", no_grade_over_100)


def demo_relations_as_sets() -> None:
    """Build a Cartesian product and a crisp relation as ordered pairs."""
    print("\n=== 3) Cartesian Product + Relation as Ordered Pairs ===")

    students = {"Ali", "Mona"}
    subjects = {"AI", "Networks"}

    cartesian_product = {(student, subject) for student in students for subject in subjects}
    likes = {("Ali", "AI"), ("Mona", "AI"), ("Mona", "Networks")}

    print("Students × Subjects =", sorted(cartesian_product))
    print("Likes relation =", sorted(likes))
    print("Does Ali like Networks?", ("Ali", "Networks") in likes)


def demo_crisp_relation_matrices() -> None:
    """Apply common set-like operations to Boolean relation matrices."""
    print("\n=== 4) Crisp Relation Matrices ===")

    r = np.array([[1, 0], [1, 1]], dtype=bool)
    s = np.array([[0, 1], [1, 0]], dtype=bool)

    union = np.logical_or(r, s)
    intersection = np.logical_and(r, s)
    complement_r = np.logical_not(r)
    inverse_r = r.T  # Inverse relation = transpose of the relation matrix.

    print("R union S:\n", union.astype(int))
    print("R intersection S:\n", intersection.astype(int))
    print("Complement of R:\n", complement_r.astype(int))
    print("Inverse of R (= transpose):\n", inverse_r.astype(int))


def boolean_relation_composition(r: np.ndarray, s: np.ndarray) -> np.ndarray:
    """Return Boolean relation composition using OR-of-ANDs.

    For every output cell T[i, j], combine all intermediate k values:
        T[i, j] = OR_k (R[i, k] AND S[k, j])
    """
    if r.shape[1] != s.shape[0]:
        raise ValueError("Inner dimensions must match for relation composition.")

    result = np.zeros((r.shape[0], s.shape[1]), dtype=bool)

    for i in range(r.shape[0]):
        for j in range(s.shape[1]):
            result[i, j] = any(
                r[i, k] and s[k, j]
                for k in range(r.shape[1])
            )

    return result


def demo_crisp_composition() -> None:
    """Demonstrate Boolean composition of two crisp relation matrices."""
    print("\n=== 5) Crisp Relation Composition ===")

    r = np.array([[1, 0, 1], [0, 1, 1]], dtype=bool)
    s = np.array([[1, 0], [0, 1], [1, 1]], dtype=bool)

    composition = boolean_relation_composition(r, s)
    print(composition.astype(int))


def max_min_composition(r: np.ndarray, s: np.ndarray) -> np.ndarray:
    """Return fuzzy max-min composition using explicit loops.

    Formula:
        T[i, j] = max_k min(R[i, k], S[k, j])

    The MIN step measures the strength of one path through k.
    The MAX step selects the strongest available path.
    """
    if r.shape[1] != s.shape[0]:
        raise ValueError("Inner dimensions must match for max-min composition.")

    result = np.zeros((r.shape[0], s.shape[1]), dtype=float)

    for i in range(r.shape[0]):
        for j in range(s.shape[1]):
            path_strengths = [
                min(r[i, k], s[k, j])
                for k in range(r.shape[1])
            ]
            result[i, j] = max(path_strengths)

    return result


def max_min_composition_vectorized(r: np.ndarray, s: np.ndarray) -> np.ndarray:
    """Return max-min composition using NumPy broadcasting.

    Shape transformation:
      R: (m, n) -> (m, n, 1)
      S: (n, p) -> (1, n, p)

    np.minimum creates all pairwise MIN values with shape (m, n, p).
    Taking MAX over axis=1 removes the intermediate n dimension and returns
    the final composition matrix with shape (m, p).
    """
    if r.shape[1] != s.shape[0]:
        raise ValueError("Inner dimensions must match for max-min composition.")

    pairwise_minimums = np.minimum(r[:, :, None], s[None, :, :])
    return np.max(pairwise_minimums, axis=1)


def demo_fuzzy_composition() -> None:
    """Compare loop-based and vectorized max-min composition."""
    print("\n=== 6) Fuzzy Max-Min Composition ===")

    r = np.array([[0.2, 0.8], [0.7, 0.4]])
    s = np.array([[0.9, 0.3], [0.5, 1.0]])

    loop_result = max_min_composition(r, s)
    vectorized_result = max_min_composition_vectorized(r, s)

    print("Loop version:\n", loop_result)
    print("Vectorized version:\n", vectorized_result)

    # allclose is preferred for floating-point arrays because tiny rounding
    # differences can make direct equality unreliable.
    assert np.allclose(loop_result, vectorized_result)


def demo_ai_matching() -> None:
    """Use max-min composition for a small Students->Skills->Jobs example."""
    print("\n=== 7) AI Matching Example: Students -> Skills -> Jobs ===")

    student_skill = np.array([
        [0.9, 0.8],  # Ahmed: Programming, Math
        [0.6, 0.9],  # Mona: Programming, Math
    ])

    skill_job = np.array([
        [0.8, 0.9],  # Programming -> AI Engineer, Web
        [1.0, 0.4],  # Math        -> AI Engineer, Web
    ])

    match = max_min_composition(student_skill, skill_job)
    job_names = ["AI Engineer", "Web"]

    print("Matching matrix:\n", match)
    print("Ahmed strongest match:", job_names[np.argmax(match[0])])
    print("Mona strongest match:", job_names[np.argmax(match[1])])


if __name__ == "__main__":
    demo_boolean_logic()
    demo_predicates_and_quantifiers()
    demo_relations_as_sets()
    demo_crisp_relation_matrices()
    demo_crisp_composition()
    demo_fuzzy_composition()
    demo_ai_matching()
