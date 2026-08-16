---
name: classical-and-quantum-information-theory
description: >-
  Provides tools, mathematical equations, and Python scripts for Classical and Quantum Information Theory (Shannon Entropy, Fisher Information Metric, KL Divergence, Mutual Information, Rate-Distortion, Information Geometry). Use when evaluating metric capacities, channel capacities, data dissipation, or statistical geometry.
---

# Classical & Quantum Information Theory Engine

This skill equips the agent to perform symbolic and numerical calculations in **Information Theory**, **Information Geometry**, and **Statistical Thermodynamics**.

## Capabilities

1. **Shannon Entropy & Mutual Information**:
   - **Shannon Entropy**: $H(X) = -\sum_{x} P(x) \log_2 P(x)$
   - **Joint Entropy**: $H(X, Y) = -\sum_{x, y} P(x, y) \log_2 P(x, y)$
   - **Mutual Information**: $I(X; Y) = H(X) + H(Y) - H(X, Y) = D_{\text{KL}}(P(X,Y) \parallel P(X)P(Y))$

2. **Kullback-Leibler (KL) Divergence & Relative Entropy**:
   - **KL Divergence**: $D_{\text{KL}}(P \parallel Q) = \sum_x P(x) \log_2 \frac{P(x)}{Q(x)}$
   - Measuring epistemic distance and probability distributions divergence under flow transitions.

3. **Fisher Information Matrix (Information Geometry)**:
   - Metric tensor $g_{ij}(\theta)$ defined on statistical manifolds of probability distributions:
     $$g_{ij}(\theta) = \mathbb{E}\left[ \frac{\partial \ln p(x;\theta)}{\partial \theta^i} \frac{\partial \ln p(x;\theta)}{\partial \theta^j} \right] = -\mathbb{E}\left[ \frac{\partial^2 \ln p(x;\theta)}{\partial \theta^i \partial \theta^j} \right]$$

4. **Rate-Distortion Theory & Channel Capacity**:
   - **Channel Capacity**: $C = \max_{P(x)} I(X; Y)$
   - **Rate-Distortion Bound**: $R(D) = \min_{P(\hat{x}|x): \mathbb{E}[d(x,\hat{x})] \le D} I(X; \hat{X})$

## Usage Guidelines

Use the Python script `info_theory_engine.py` in the `scripts/` directory to calculate Shannon entropy, KL divergence, and Fisher Information.

[info_theory_engine.py](./scripts/info_theory_engine.py)

```python
import sympy as sp
from info_theory_engine import InformationTheoryEngine

ite = InformationTheoryEngine()

# Probability distribution
P = [0.5, 0.25, 0.25]
Q = [0.333, 0.333, 0.334]

shannon_H = ite.shannon_entropy(P)
kl_div = ite.kl_divergence(P, Q)

print("Shannon Entropy (bits):", shannon_H)
print("KL Divergence D_KL(P||Q):", kl_div)
```
