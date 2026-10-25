# Fuzzy Logic Practical Sessions

A clean, classroom-oriented collection of Python demos for practical topics in **Fuzzy Logic / Soft Computing**. The examples progress from membership functions and crisp logic to fuzzy-set properties, relations, composition, and fuzzy-set operations.

## Topics Covered

| Section | Topic | Main files |
|---|---|---|
| 01 | Membership Functions & Fuzzification | `temperature_membership_functions.py`, `temperature_membership_degree.py` |
| 02 | Boolean Logic, Relations & Composition | `logic_relations_and_composition_demo.py`, `max_min_composition_step_by_step.py` |
| 03 | Fuzzy Set Properties | `fuzzy_set_properties_demo.py` |
| 04 | Fuzzy Set Operations | `discrete_fuzzy_set_operations.py`, `triangular_membership_function.py`, `visualize_fuzzy_operations.py`, `student_practice.py` |

## Project Structure

```text
fuzzy-logic-practical-sessions/
├── README.md
├── REVIEW_REPORT.md
├── requirements.txt
├── .gitignore
├── section_01_membership_functions/
│   ├── temperature_membership_functions.py
│   └── temperature_membership_degree.py
├── section_02_logic_and_relations/
│   ├── logic_relations_and_composition_demo.py
│   └── max_min_composition_step_by_step.py
├── section_03_fuzzy_set_properties/
│   └── fuzzy_set_properties_demo.py
└── section_04_fuzzy_set_operations/
    ├── fuzzy_operations.py
    ├── discrete_fuzzy_set_operations.py
    ├── triangular_membership_function.py
    ├── visualize_fuzzy_operations.py
    └── student_practice.py
```

## Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd fuzzy-logic-practical-sessions
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Examples

### Section 01 — Membership Functions

```bash
python section_01_membership_functions/temperature_membership_functions.py
python section_01_membership_functions/temperature_membership_degree.py
```

The first script compares triangular, trapezoidal, and Gaussian membership functions. The second demonstrates **fuzzification** by evaluating the membership degrees of one crisp temperature.

### Section 02 — Logic, Relations, and Composition

```bash
python section_02_logic_and_relations/logic_relations_and_composition_demo.py
python section_02_logic_and_relations/max_min_composition_step_by_step.py
```

The step-by-step composition example prints every `min(...)` calculation before applying `max(...)`, making the **max-min composition** easy to explain in a lab.

### Section 03 — Fuzzy Set Properties

```bash
python section_03_fuzzy_set_properties/fuzzy_set_properties_demo.py
```

This example calculates:

- Support
- Boundary
- Crossover points
- Core
- Bandwidth
- Alpha-cut and strong alpha-cut
- Cardinality and relative cardinality
- Symmetry
- Convexity
- Fuzzy singleton status

### Section 04 — Fuzzy Set Operations

```bash
python section_04_fuzzy_set_operations/discrete_fuzzy_set_operations.py
python section_04_fuzzy_set_operations/triangular_membership_function.py
python section_04_fuzzy_set_operations/visualize_fuzzy_operations.py
python section_04_fuzzy_set_operations/student_practice.py
```

The reusable module `fuzzy_operations.py` implements:

- Standard Complement
- Standard Union using `MAX`
- Standard Intersection using `MIN`
- Algebraic Product
- Algebraic Sum
- Bounded Sum
- Bounded Difference

A key observation demonstrated in the code is:

```text
Algebraic Product <= MIN Intersection
```

for membership values in `[0, 1]`.

## Teaching Notes

The code is intentionally written for teaching rather than maximum compactness. Difficult operations include comments explaining the mathematical idea behind the implementation, especially:

- Predicates and quantifiers with `all()` and `any()`
- Boolean relation composition
- Fuzzy max-min composition
- NumPy broadcasting in vectorized max-min composition
- Alpha-cuts and fuzzy cardinality
- Discrete symmetry and convexity checks
- Comparison between `MIN` intersection and Algebraic Product

## Suggested Practical Flow

1. Explain the mathematical definition.
2. Calculate a small example manually.
3. Run the corresponding Python script.
4. Compare the code output with the manual result.
5. Use the plotting examples to visualize the concept.
6. Let students modify membership values or function parameters and observe the effect.

## Requirements

- Python 3.10+
- NumPy
- Matplotlib
- scikit-fuzzy

Install everything with:

```bash
pip install -r requirements.txt
```

## Notes

- Membership degrees are expected to stay in the interval `[0, 1]`.
- The Section 03 convexity check is a simplified discrete check intended for the current ordered, single-peaked classroom example.
- Plotting scripts open Matplotlib windows; when running on a headless environment, use an appropriate Matplotlib backend.
