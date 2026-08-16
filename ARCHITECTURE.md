# 🏛️ Aetherius Engine Architectural Specification (PMCA v6.0)

## 1. Mathematical Substrate: 3D Conal Cylindrical Metric Space

The Pure Mathematical Conal Architecture (PMCA) represents semantic states as metric tensor fields over a 3D conal cylindrical manifold $\mathcal{M}$.

In cylindrical coordinates $(z, r, \theta)$, the metric tensor field $\mathbf{g}(z, r, \theta)$ defines the infinitesimal squared distance:

$$ds^2 = g_{ij} dx^i dx^j = g_{zz} dz^2 + g_{rr} dr^2 + g_{\theta\theta} d\theta^2 + 2g_{zr} dz dr + 2g_{z\theta} dz d\theta + 2g_{r\theta} dr d\theta$$

### Tapered Conal Constraint
To enforce causality and semantic hierarchy along the depth axis $z \in [0, Z_{\max}]$, the radial coordinate $r$ is bounded by a tapering function $R(z)$:

$$R(z) = R_0 \left(1 - \frac{z}{Z_{\max}}\right)^\gamma, \quad \gamma > 0$$

As $z \to Z_{\max}$, the manifold tapers down to an apex point representing high-level semantic abstraction.

---

## 2. Information-Geometric Ricci-Fisher Flow Engine

Logical contradictions and semantic ambiguities manifest as curvature singularities or topological anomalies in the metric $\mathbf{g}$. PMCA resolves these contradictions by driving the metric through a generalized **Ricci-Fisher Flow**:

$$\frac{\partial g_{ij}}{\partial \tau} = -2 R_{ij} + \alpha F_{ij}$$

where:
- $R_{ij}$ is the **Ricci Curvature Tensor**, derived from the Christoffel symbols $\Gamma^\mu_{\alpha\beta}$.
- $F_{ij}$ is the **Fisher Information Metric**, capturing statistical density variations.
- $\alpha > 0$ is the information-geometric coupling constant.
- $\tau$ is fictitious intrinsic flow time.

### DeTurck Positive-Definiteness Projection
To prevent manifold collapse ($\det(\mathbf{g}) \to 0$) or signature inversion during integration, the DeTurck modification projects the metric at each step:

$$\mathbf{g}(\tau + \Delta \tau) \leftarrow \mathbf{g}(\tau) + \Delta \tau \cdot \operatorname{Proj}_{\text{PD}}\left( -2\mathbf{R} + \alpha \mathbf{F} \right)$$

ensuring $\lambda_{\min}(\mathbf{g}) \ge \epsilon > 0$.

---

## 3. Thermodynamic Autopoiesis & Motor Cortex

PMCA introduces **Thermodynamic Autopoiesis** as an intrinsic drive mechanism. 

```text
[Input Query] ---> [Marcus Kracht Sign Tree S=(A,C,M)]
                           |
                           v
                [Metric Tensor Field g_ij]
                           |
                           v
              [Persistent Homology Engine]
                           |
                           v
                Does Betti_1 > 0 exist?
               /                       \
        (No: Harmony)            (Yes: Paradox)
             |                          |
    [Output Translation]       [Entropy Spike ΔS > λ]
                                        |
                                        v
                            [Autopoietic Motor Cortex]
                                        |
                                        v
                       [API Execution: AlphaFold/PubMed]
```

When a self-referential paradox or logical contradiction enters the manifold:
1. The Topological Data Analysis (TDA) module detects non-trivial 1D homology cycles ($Betti_1 > 0$).
2. The presence of $Betti_1 > 0$ causes an instant spike in **Shannon Entropy** $S(\mathbf{g})$.
3. When $\Delta S > \lambda_{\text{threshold}}$, the engine actuates the **Autopoietic Motor Cortex**.
4. The Motor Cortex executes scientific API queries (e.g., AlphaFold, PubMed, Astropy) to pull external ground-truth data.
5. The retrieved data is injected as **Topological Mass** into the metric tensor adjacency matrix.
6. The hole collapses ($Betti_1 \to 0$), Shannon entropy returns to baseline harmony, and the flow converges cleanly.

---

## 4. Hardware Acceleration (JAX/XLA)

The core operations (`geometry.py`, `flow.py`, `autopoiesis.py`) are implemented using JAX/XLA primitives:
- `@jax.jit` compiled Ricci-Fisher flow integration loop.
- `vmap` vectorized tensor field updates across $100\text{B}+$ particle grids.
- Zero-copy memory layout targeting GPU/TPU memory bandwidth.

---

## 5. Mathematical Tightening & Completeness Specifications

PMCA v6.0 formally enforces four mathematical bounds:

1. **Curvature Bounds ($|R_{ij}| \le K_{\max}$):**
   Sections of high curvature are bounded by continuous DeTurck eigenvalue clipping, guaranteeing smooth tensor integration without numerical or metric blow-ups.

2. **Amari Fisher Information Metric ($F_{ij}$):**
   The Fisher term $F_{ij} = \frac{\partial^2 D_{\text{KL}}}{\partial \theta^i \partial \theta^j}$ is formally derived as the natural gradient metric tensor induced by relative entropy on statistical manifolds.

3. **Fermi-Dirac Autopoietic Threshold Calibration ($\chi(T)$):**
   The autopoietic activation probability is modeled via an adaptive Fermi-Dirac distribution:
   $$\chi(S, T_{\text{info}}) = \frac{1}{1 + \exp\left( -\frac{\beta (S - S_{\text{crit}})}{T_{\text{info}}} \right)}$$

4. **Geodesic Manifold Completeness (Hopf-Rinow Theorem):**
   Apex regularization is achieved via a smooth capping function $R_{\text{capped}}(z) = R_0 \max(1 - z/Z_{\max}, \varepsilon_{\text{cap}})^\gamma$, guaranteeing that $(\overline{\mathcal{M}}, \mathbf{g})$ is geodesically complete for all continuous flow times $\tau \in [0, \infty)$.
