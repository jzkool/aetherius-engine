import jax
import jax.numpy as jnp

class RicciFisherFlow:
    """
    Information-Geometric Ricci-Fisher Flow Engine:
    dg/dtau = -2 * R_ij + alpha * F_ij
    Includes DeTurck Projection for Positive-Definiteness bounds.
    """
    def __init__(self, alpha=0.1, dt=0.01, min_eigenvalue=1e-4):
        self.alpha = alpha
        self.dt = dt
        self.min_eigenvalue = min_eigenvalue

    @staticmethod
    @jax.jit
    def step_jit(g, R, F, alpha, dt, min_ev):
        """
        XLA JIT-compiled Ricci-Fisher Integration Step
        """
        dg = -2.0 * R + alpha * F
        g_new = g + dt * dg
        
        # DeTurck Projection: Enforce Positive-Definiteness
        eigvals, eigvecs = jnp.linalg.eigh(g_new)
        bounded_eigvals = jnp.maximum(eigvals, min_ev)
        g_proj = eigvecs @ jnp.diag(bounded_eigvals) @ eigvecs.T
        return g_proj

    def step(self, g, R=None, F=None):
        if R is None:
            R = jnp.zeros_like(g)
        if F is None:
            F = jnp.ones_like(g)
            
        return self.step_jit(g, R, F, self.alpha, self.dt, self.min_eigenvalue)
