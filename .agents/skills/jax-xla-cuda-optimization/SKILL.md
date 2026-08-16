---
name: jax-xla-cuda-optimization
description: >-
  Provides patterns, performance optimizations, and Python scripts for JAX, XLA compilation, CUDA GPU/TPU acceleration, vectorized operations (vmap/pmap), custom autograd (custom_vjp), and low-latency tensor processing. Use when optimizing numerical pipelines, tensor operations, or training/inference loops for maximum throughput.
---

# JAX, XLA & CUDA High-Performance Optimization Engine

This skill equips the agent with software engineering patterns for high-throughput, hardware-accelerated tensor computations using **JAX**, **XLA**, and **CUDA/TPU** architectures.

## Key Optimization Patterns

1. **XLA Just-In-Time (JIT) Compilation (`@jax.jit`)**:
   Eliminates Python overhead by fusing array operations into optimized GPU/TPU machine code.
   - *Rule*: Avoid dynamic array shapes; keep shapes static across calls to prevent re-compilation.

2. **Vectorization & Auto-Batching (`@jax.vmap`)**:
   Maps single-sample tensor functions across arbitrary batch dimensions without manual slicing.

3. **Multi-Device / TPU Parallelism (`@jax.pmap`)**:
   Distributes batch dimensions across multiple GPU/TPU cores using collective communications (`pmean`, `psum`).

4. **Custom Derivatives & Vector-Jacobian Products (`jax.custom_vjp`)**:
   Defines custom reverse-mode automatic differentiation rules to preserve stability during matrix inversions or differential geometry Ricci flows.

## Usage Example

Use `jax_optimizer_template.py` in `scripts/` to profile and execute JIT-compiled tensor operations.

[jax_optimizer_template.py](./scripts/jax_optimizer_template.py)

```python
import jax
import jax.numpy as jnp

@jax.jit
def ricci_step(g, R, alpha, F):
    """
    XLA JIT-compiled Ricci-Fisher Integration Step:
    dg/dtau = -2 R + alpha * F
    """
    return g + 0.01 * (-2.0 * R + alpha * F)

# Initialize sample 3x3 metric on GPU/TPU
g = jnp.eye(3)
R = jnp.zeros((3, 3))
F = jnp.ones((3, 3))

g_next = ricci_step(g, R, 0.1, F)
print("Updated Metric:\n", g_next)
```
