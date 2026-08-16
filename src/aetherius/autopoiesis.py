import jax
import jax.numpy as jnp

class AutopoieticCortex:
    """
    Thermodynamic Autopoiesis Module (PMCA v6.0):
    Monitors Shannon/von Neumann Entropy S and Betti_1 homology cycles.
    Actuates external scientific API tools via an adaptive Fermi-Dirac threshold function chi(T).
    """
    def __init__(self, entropy_threshold=0.75, beta=5.0, T_ref=1.0):
        self.entropy_threshold = entropy_threshold
        self.beta = beta
        self.T_ref = T_ref

    def calculate_shannon_entropy(self, metric_tensor):
        """Calculates normalized Shannon Entropy from metric eigenvalues"""
        eigvals = jnp.linalg.eigvalsh(metric_tensor)
        p = jnp.abs(eigvals) / jnp.sum(jnp.abs(eigvals))
        p = jnp.maximum(p, 1e-12)
        return -jnp.sum(p * jnp.log2(p))

    def chi_threshold(self, entropy, T_info=1.0):
        """
        Empirically Calibrated Autopoietic Threshold Function chi(T):
        Fermi-Dirac sigmoidal transition probability P_actuate = 1 / (1 + exp(-beta * (S - S_crit) / T_info))
        """
        delta_S = entropy - self.entropy_threshold
        arg = -self.beta * delta_S / jnp.maximum(T_info, 1e-5)
        return 1.0 / (1.0 + jnp.exp(jnp.clip(arg, -50.0, 50.0)))

    def evaluate_state(self, metric_tensor, betti_1_count=0, T_info=1.0):
        """
        Evaluates thermodynamic harmony using calibrated chi(T) function.
        """
        entropy = self.calculate_shannon_entropy(metric_tensor)
        actuation_prob = float(self.chi_threshold(entropy, T_info))
        
        needs_actuation = (actuation_prob > 0.5) or (betti_1_count > 0)
        
        return {
            "entropy": float(entropy),
            "betti_1": betti_1_count,
            "actuation_probability": actuation_prob,
            "actuate_motor_cortex": bool(needs_actuation),
            "status": "HARMONY" if not needs_actuation else "PARADOX_DETECTED"
        }
