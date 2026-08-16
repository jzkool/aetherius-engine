import jax
import jax.numpy as jnp

class ConalMetric:
    """
    Implements the 3D Conal Cylindrical Metric Tensor Substrate: g(z, r, theta)
    g_ij = diag(1 + z/z_max, 1.0, r(z)^2 * (1 + 0.1 * cos(theta)))
    """
    def __init__(self, z_max=10.0, r_initial=1.0, gamma=0.5):
        self.z_max = z_max
        self.r_0 = r_initial
        self.gamma = gamma

    def radial_taper(self, z):
        """Calculates tapered boundary radius R(z) = R_0 * (1 - z/Z_max)^gamma"""
        return self.r_0 * jnp.power(jnp.maximum(1.0 - z / self.z_max, 1e-5), self.gamma)

    def compute_tensor(self, z, r, theta):
        """
        Computes 3x3 metric tensor g_ij in cylindrical coordinates (z, r, theta).
        """
        g_zz = 1.0 + (z / self.z_max)
        g_rr = 1.0
        g_tt = (r ** 2) * (1.0 + 0.1 * jnp.cos(theta))
        
        return jnp.diag(jnp.array([g_zz, g_rr, g_tt]))
