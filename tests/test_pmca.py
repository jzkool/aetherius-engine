import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
import jax.numpy as jnp
from aetherius.geometry import ConalMetric
from aetherius.flow import RicciFisherFlow
from aetherius.autopoiesis import AutopoieticCortex

class TestPMCAEngine(unittest.TestCase):
    """
    Automated Unit Test Suite for PMCA Engine Core.
    """
    def setUp(self):
        self.metric = ConalMetric(z_max=10.0)
        self.flow = RicciFisherFlow(alpha=0.1, dt=0.01)
        self.cortex = AutopoieticCortex(entropy_threshold=0.75)

    def test_conal_metric_positive_definiteness(self):
        """Test that metric tensor eigenvalues are strictly positive."""
        g = self.metric.compute_tensor(z=5.0, r=1.0, theta=0.0)
        eigvals = jnp.linalg.eigvalsh(g)
        self.assertTrue(jnp.all(eigvals > 0), "Metric tensor is not positive definite!")

    def test_ricci_fisher_step(self):
        """Test that Ricci-Fisher flow updates metric without NaN/Inf."""
        g = self.metric.compute_tensor(z=2.0, r=1.0, theta=0.0)
        g_next = self.flow.step(g)
        self.assertFalse(jnp.isnan(g_next).any(), "Ricci flow returned NaN!")
        self.assertFalse(jnp.isinf(g_next).any(), "Ricci flow returned Inf!")

    def test_autopoietic_actuation(self):
        """Test entropy calculation and autopoietic actuation triggering."""
        g = self.metric.compute_tensor(z=1.0, r=1.0, theta=0.0)
        res = self.cortex.evaluate_state(g, betti_1_count=1)
        self.assertTrue(res["actuate_motor_cortex"])
        self.assertEqual(res["status"], "PARADOX_DETECTED")

if __name__ == '__main__':
    unittest.main()
