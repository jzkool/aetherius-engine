---
name: quantum-information-and-mechanics
description: >-
  Provides tools, mathematical equations, and Python scripts for Quantum Mechanics, Hilbert Spaces, Density Matrices, Quantum Entanglement, von Neumann Entropy, Unitary Evolution, and Quantum Computing. Use when evaluating quantum states, density matrix purities, entanglement measures, or quantum information metrics.
---

# Quantum Information & Quantum Mechanics Engine

This skill equips the agent to perform symbolic and numerical calculations in **Quantum Mechanics**, **Quantum Information Theory**, and **Quantum Computing**.

## Capabilities

1. **State Vectors & Density Matrices**:
   - **Pure States**: $|\psi\rangle \in \mathcal{H}$
   - **Mixed States / Density Operator**: $\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$, with $\operatorname{Tr}(\rho) = 1$ and $\rho \ge 0$.
   - **Purity**: $\gamma = \operatorname{Tr}(\rho^2)$. ($\gamma = 1$ for pure states, $\gamma < 1$ for mixed states).

2. **von Neumann Entropy & Quantum Entanglement**:
   - **von Neumann Entropy**: $S(\rho) = -\operatorname{Tr}(\rho \log_2 \rho) = -\sum \lambda_i \log_2 \lambda_i$ where $\lambda_i$ are the eigenvalues of $\rho$.
   - **Entanglement Entropy**: $S(\rho_A) = -\operatorname{Tr}(\rho_A \log_2 \rho_A)$ derived from the partial trace $\rho_A = \operatorname{Tr}_B(\rho_{AB})$.

3. **Quantum Dynamics & Unitary Evolution**:
   - **Schrödinger Equation**: $i\hbar \frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H} |\psi(t)\rangle$
   - **Von Neumann / Liouville-von Neumann Equation**: $\frac{\partial \rho}{\partial t} = -\frac{i}{\hbar} [\hat{H}, \rho]$
   - **Quantum Fidelity**: $F(\rho, \sigma) = \left( \operatorname{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}} \right)^2$

4. **Bloch Sphere & Qubit Gates**:
   - Qubit State: $|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$
   - Pauli Spin Matrices $\sigma_x, \sigma_y, \sigma_z$ and Hadamard, CNOT, Phase gates.

## Usage Guidelines

Use the Python script `quantum_info_engine.py` in the `scripts/` directory to evaluate density matrices, purity, von Neumann entropy, and partial traces.

[quantum_info_engine.py](./scripts/quantum_info_engine.py)

```python
import sympy as sp
from quantum_info_engine import QuantumInformationEngine

qie = QuantumInformationEngine()

# Define a maximally mixed 2-qubit density matrix
rho_mixed = sp.Matrix.diag(0.25, 0.25, 0.25, 0.25)

purity = qie.purity(rho_mixed)
entropy = qie.von_neumann_entropy(rho_mixed)

print("Purity:", purity)
print("von Neumann Entropy (bits):", entropy)
```
