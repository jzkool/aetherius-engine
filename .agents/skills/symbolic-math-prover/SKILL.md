---
name: symbolic-math-prover
description: >-
  Provides tools, instructions, and scripts for mathematically proving theorems, computing derivatives, solving integrals, and verifying differential geometry tensors (Christoffel, Ricci, Laplacian) using SymPy and SciPy. Use this skill when verifying continuous metric updates, eigenvalues, or thermodynamic topologies.
---

# Symbolic Math Prover

This skill empowers the agent to act as a rigorous mathematical prover. It leverages Python, specifically `sympy`, to verify equations, compute exact symbolic derivatives, solve differential equations, and evaluate geometric tensors.

## Capabilities

1. **Symbolic Calculus**: Exact derivatives, integrals, and limits without floating-point errors.
2. **Differential Geometry Verification**: Automated computation of Christoffel symbols, Ricci curvature tensors, and scalar curvature given an initial metric tensor $g_{ij}$.
3. **Spectral / Eigenvalue Bounding**: Verifying positive-definiteness and Lyapunov functional dissipation rates.
4. **Equation Solving**: Roots and ODE integration.

## Usage Guidelines

Whenever the user asks you to "verify the math", "prove the manifold properties", or "compute the derivatives", you should write a short Python script leveraging `sympy` to definitively prove the result.

### 1. Basic Symbolic Proofs
Use `sympy` for exact verification.

```python
import sympy as sp

x, y, t = sp.symbols('x y t')
f = sp.exp(-t) * (x**2 + y**2)

# Compute partial derivatives
df_dx = sp.diff(f, x)
df_dt = sp.diff(f, t)

print(f"df/dx = {df_dx}")
print(f"df/dt = {df_dt}")
```

### 2. Differential Geometry Helper Script
For Riemannian geometry (Metric Tensors, Christoffel Symbols, Ricci Flow), use the provided helper script rather than writing the tensor contractions from scratch.

[verify_geometry.py](./scripts/verify_geometry.py)

**Usage Example:**
```python
import sympy as sp
from verify_geometry import GeometryProver

# Define symbols
r, theta, phi = sp.symbols('r theta phi')
coords = [r, theta, phi]

# Define a diagonal metric tensor
g_matrix = sp.Matrix([
    [1, 0, 0],
    [0, r**2, 0],
    [0, 0, r**2 * sp.sin(theta)**2]
])

prover = GeometryProver(coords, g_matrix)
christoffel = prover.christoffel_symbols()
ricci = prover.ricci_tensor()
scalar = prover.ricci_scalar()

print(f"Ricci Scalar: {scalar}")
```

### 3. Verification of Positive-Definiteness (Lyapunov/Laplacian)
To prove eigenvalue bounds, use `scipy.linalg` or `sympy.eigenvals`.

```python
import sympy as sp
M = sp.Matrix([[2, -1], [-1, 2]])
eigenvalues = M.eigenvals()
print("Eigenvalues:", eigenvalues)
# Prove positive definite
assert all(sp.re(val) > 0 for val in eigenvalues.keys())
```

## Setup & Dependencies
Ensure the environment has `sympy`, `scipy`, and `numpy` installed. If they are missing, install them via:
`uv pip install sympy scipy numpy` or `pip install sympy scipy numpy`
