---
name: theoretical-physics-engine
description: >-
  Provides tools, mathematical equations, and Python scripts for General Relativity (GR), Astrophysics, Relativistic Geodesics, and Cosmology (FLRW metric, Schwarzschild event horizons, Einstein Field Equations, Energy-Momentum tensor). Use when analyzing spacetime metrics, gravitational curvature, cosmic scaling, or astrophysical geodesics.
---

# Theoretical Physics & General Relativity Engine

This skill equips the agent to perform exact symbolic and numerical computations in **General Relativity**, **Astrophysics**, and **Cosmology**.

## Capabilities

1. **Einstein Field Equations & Curvature**:
   $$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$
   Computes the Einstein Tensor $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu}$ from any spacetime metric tensor $g_{\mu\nu}$.

2. **Astrophysical Black Hole Metrics**:
   - **Schwarzschild Metric** (Non-rotating black holes):
     $$ds^2 = -\left(1 - \frac{r_s}{r}\right) c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 + r^2 (d\theta^2 + \sin^2\theta d\phi^2)$$
     where $r_s = \frac{2GM}{c^2}$ is the Schwarzschild radius.
   - **Photon Sphere**: $r = 1.5 r_s$
   - **Gravitational Redshift**: $z_{\text{grav}} = \left(1 - \frac{r_s}{r}\right)^{-1/2} - 1$

3. **FLRW Cosmology**:
   Friedmann-Lemaître-Robertson-Walker metric for isotropic, homogeneous expanding universes:
   $$ds^2 = -c^2 dt^2 + a(t)^2 \left[ \frac{dr^2}{1 - k r^2} + r^2 (d\theta^2 + \sin^2\theta d\phi^2) \right]$$
   Evaluates cosmic expansion scale factor $a(t)$, Hubble parameter $H(t) = \frac{\dot{a}}{a}$, luminosity distance $D_L(z)$, and cosmic age $t(z)$.

4. **Geodesic Integrator**:
   4th-order Runge-Kutta numerical integration of relativistic particle paths:
   $$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0$$

## Usage Guidelines

Use the Python script `gr_cosmology.py` located in the `scripts/` folder to automate tensor calculus for General Relativity.

[gr_cosmology.py](./scripts/gr_cosmology.py)

```python
import sympy as sp
from gr_cosmology import GeneralRelativityEngine

# Define spacetime coordinates: t, r, theta, phi
t, r, theta, phi = sp.symbols('t r theta phi')
coords = [t, r, theta, phi]
M, c, G = sp.symbols('M c G', positive=True)
r_s = 2 * G * M / c**2

# Schwarzschild metric matrix
g_schwarzschild = sp.Matrix([
    [-(1 - r_s/r) * c**2, 0, 0, 0],
    [0, 1 / (1 - r_s/r), 0, 0],
    [0, 0, r**2, 0],
    [0, 0, 0, r**2 * sp.sin(theta)**2]
])

gr = GeneralRelativityEngine(coords, g_schwarzschild)
einstein_tensor = gr.einstein_tensor()
print("Einstein Tensor G_00:", einstein_tensor[0, 0])
```
