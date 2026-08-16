---
name: software-architecture-and-design-patterns
description: >-
  Provides architectural patterns, clean code design principles, Python package structuring (pyproject.toml/pip), unit testing harnesses (pytest), and production design patterns (Factory, Strategy, Observer, Adapter). Use when building scalable software systems, refactoring codebases, or designing production SDKs.
---

# Software Architecture & Production Engineering Skill

This skill equips the agent to write production-grade, modular, and maintainable software systems.

## Architectural Principles

1. **SOLID Principles**:
   - **Single Responsibility Principle**: Each class/module handles one mathematical or execution responsibility.
   - **Open/Closed Principle**: Extend metric tensor types without altering core Ricci-flow solvers.
   - **Liskov Substitution**: Geometric solvers inherit from unified `BaseManifoldSolver` interfaces.
   - **Interface Segregation**: Keep Perception, Geometry, and Tool Calling interfaces decoupled.
   - **Dependency Inversion**: High-level Autopoietic controllers depend on abstractions (`ToolManagerInterface`), not concrete implementations.

2. **Package Layout Standard**:
   ```text
   aetherius/
   ├── src/
   │   └── aetherius/
   │       ├── __init__.py
   │       ├── core/          # Metric tensors, Lie algebra, manifolds
   │       ├── solvers/       # Ricci flow, Geodesic integrators
   │       ├── perception/    # Sign algebra, categorial parsing
   │       └── autopoiesis/   # Entropy thresholds, API tool dispatchers
   ├── tests/                 # Automated pytest unit test suite
   ├── pyproject.toml         # Modern build configuration
   └── README.md
   ```

3. **Defensive Programming & Fail-Safe Boundaries**:
   - Never swallow exceptions silently.
   - Validate numerical inputs using runtime assertions or Pydantic schemas.
   - Use explicit typing (`typing.Annotated`, `jax.typing.ArrayLike`).

## Usage Example

Use `test_harness_template.py` in `scripts/` to set up automated unit test suites with `pytest`.

[test_harness_template.py](./scripts/test_harness_template.py)

```python
import pytest
import numpy as np

def test_metric_positive_definiteness():
    """Verify that metric tensor eigenvalues are strictly positive."""
    g = np.array([[2.0, 0.5], [0.5, 1.0]])
    eigenvalues = np.linalg.eigvalsh(g)
    assert np.all(eigenvalues > 0), "Metric tensor is not positive-definite!"
```
