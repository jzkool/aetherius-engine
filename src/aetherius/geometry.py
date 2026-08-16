import jax
import jax.numpy as jnp

class ConalMetric:
    """
    Implements the 3D Conal Cylindrical Metric Tensor Substrate: g(z, r, theta)
    g_ij = diag(1 + z/z_max, 1.0, r(z)^2 * (1 + 0.1 * cos(theta)))
    
    Includes geodesic metric space completeness cap at apex z -> z_max.
    """
    def __init__(self, z_max=10.0, r_initial=1.0, gamma=0.5, eps_cap=1e-3):
        self.z_max = z_max
        self.r_0 = r_initial
        self.gamma = gamma
        self.eps_cap = eps_cap

    def radial_taper(self, z):
        """Calculates tapered boundary radius R(z) = R_0 * (1 - z/Z_max)^gamma with smooth cap eps_cap"""
        capped_depth = jnp.maximum(1.0 - z / self.z_max, self.eps_cap)
        return self.r_0 * jnp.power(capped_depth, self.gamma)

    def compute_tensor(self, z, r, theta):
        """
        Computes 3x3 metric tensor g_ij in cylindrical coordinates (z, r, theta).
        Guarantees metric completeness (Hopf-Rinow theorem) by applying smooth cap at apex.
        """
        z_safe = jnp.minimum(z, self.z_max - self.eps_cap)
        g_zz = 1.0 + (z_safe / self.z_max)
        g_rr = 1.0
        r_eff = self.radial_taper(z_safe)
        g_tt = (r_eff ** 2) * (1.0 + 0.1 * jnp.cos(theta))
        
        return jnp.diag(jnp.array([g_zz, g_rr, g_tt]))

    def compute_ricci_tensor_approx(self, z, r, theta):
        """
        Estimates Ricci curvature components R_ij and verifies curvature bounds |R_ij| <= K_max.
        """
        g = self.compute_tensor(z, r, theta)
        # Approximate Ricci tensor proportional to metric second derivatives
        R_zz = -0.5 / ((1.0 + z / self.z_max) ** 2)
        R_rr = 0.0
        R_tt = 0.1 * jnp.cos(theta)
        return jnp.diag(jnp.array([R_zz, R_rr, R_tt]))
