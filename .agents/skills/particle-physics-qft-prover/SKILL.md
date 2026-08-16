---
name: particle-physics-qft-prover
description: >-
  Provides tools, mathematical equations, and Python scripts for Quantum Field Theory (QFT), Theoretical Particle Physics, Gauge Groups (SU(3) x SU(2) x U(1)), Lie Algebras, Dirac Spinors, Gamma Matrices, and 11D Calabi-Yau Manifold Compactifications. Use when analyzing elementary particles, quantum lagrangians, gauge symmetries, or string compactifications.
---

# Theoretical Particle Physics & Quantum Field Theory (QFT) Prover

This skill equips the agent to perform symbolic calculations in **Quantum Field Theory (QFT)**, **Gauge Theories**, and **High-Energy Theoretical Particle Physics**.

## Capabilities

1. **Standard Model Gauge Group $SU(3)_C \times SU(2)_L \times U(1)_Y$**:
   - **$U(1)_Y$ Hypercharge**: Phase transformations $\psi \to e^{i \alpha Y} \psi$.
   - **$SU(2)_L$ Weak Isospin**: Pauli matrices $\sigma^i$, doublet fields, W/Z boson mass generation via the Higgs mechanism.
   - **$SU(3)_C$ Quantum Chromodynamics (QCD)**: 8 Gell-Mann matrices $\lambda^a$, color octet gluons, structure constants $f^{abc}$.

2. **Dirac Spinors & Clifford Algebra**:
   Evaluates Dirac Gamma matrices $\gamma^\mu$ satisfying $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu} I_4$:
   - **Dirac Equation**: $(i \gamma^\mu \partial_\mu - m)\psi = 0$
   - **Chirality Projections**: $P_L = \frac{1 - \gamma^5}{2}$, $P_R = \frac{1 + \gamma^5}{2}$
   - **Feynman Diagram Traces**: $\operatorname{Tr}(\gamma^\mu \gamma^\nu \gamma^\rho \gamma^\sigma) = 4(g^{\mu\nu}g^{\rho\sigma} - g^{\mu\rho}g^{\nu\sigma} + g^{\mu\sigma}g^{\nu\rho})$

3. **Yang-Mills Lagrangians & Gauge Covariance**:
   $$\mathcal{L}_{\text{YM}} = -\frac{1}{4} F^a_{\mu\nu} F^{a\mu\nu}, \quad F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + g f^{abc} A^b_\mu A^c_\nu$$

4. **11D Supergravity & Calabi-Yau Compactification**:
   Models 11D M-Theory spacetime compactified on a 6D Calabi-Yau manifold $\mathcal{M}_6$ with Ricci-flat metric ($R_{i\bar{j}} = 0$) and $SU(3)$ holonomy, reducing 11D gravity to 4D effective field theories with $\mathcal{N}=1$ supersymmetry.

## Usage Guidelines

Use the Python script `qft_algebra.py` located in the `scripts/` folder to compute Dirac gamma traces, Pauli matrix commutators, and Lie algebra structure constants.

[qft_algebra.py](./scripts/qft_algebra.py)

```python
import sympy as sp
from qft_algebra import QFTAlgebraEngine

qft = QFTAlgebraEngine()

# Compute Dirac Gamma Matrix Trace
trace_val = qft.dirac_trace_4gamma(mu=0, nu=1, rho=0, sigma=1)
print("Trace(gamma^0 gamma^1 gamma^0 gamma^1):", trace_val)

# Evaluate Gell-Mann Matrix Commutator [lambda_1, lambda_2]
comm = qft.gellmann_commutator(1, 2)
print("[lambda_1, lambda_2] =", comm)
```
