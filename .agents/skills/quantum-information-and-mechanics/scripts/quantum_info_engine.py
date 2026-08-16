import sympy as sp

class QuantumInformationEngine:
    """
    Symbolic evaluation engine for Quantum Information, Density Matrices,
    von Neumann Entropy, Purity, and Partial Traces.
    """
    def __init__(self):
        self.hbar = sp.Symbol('hbar', positive=True)

    def purity(self, density_matrix):
        """Calculates purity gamma = Tr(rho^2)"""
        rho2 = density_matrix * density_matrix
        return sp.simplify(rho2.trace())

    def von_neumann_entropy(self, density_matrix, base=2):
        """Calculates von Neumann entropy S(rho) = -Tr(rho log(rho))"""
        eigenvals = density_matrix.eigenvals()
        entropy = 0
        for val, mult in eigenvals.items():
            if val > 0:
                if base == 2:
                    entropy -= mult * val * sp.log(val, 2)
                else:
                    entropy -= mult * val * sp.log(val)
        return sp.simplify(entropy)

    def is_valid_density_matrix(self, density_matrix):
        """Verifies if rho is positive semi-definite and has unit trace"""
        trace_ok = sp.simplify(density_matrix.trace()) == 1
        eigenvals = density_matrix.eigenvals()
        pos_ok = all(sp.re(val) >= 0 for val in eigenvals.keys())
        return trace_ok and pos_ok

    def partial_trace_2qubit(self, density_matrix_4x4, trace_over='B'):
        """
        Computes partial trace of a 4x4 2-qubit system.
        If trace_over=='B', returns 2x2 rho_A = Tr_B(rho_AB)
        If trace_over=='A', returns 2x2 rho_B = Tr_A(rho_AB)
        """
        rho = density_matrix_4x4
        if trace_over.upper() == 'B':
            # Block 2x2 entries: rho_A[i, j] = rho[2*i, 2*j] + rho[2*i+1, 2*j+1]
            r00 = rho[0, 0] + rho[1, 1]
            r01 = rho[0, 2] + rho[1, 3]
            r10 = rho[2, 0] + rho[3, 1]
            r11 = rho[2, 2] + rho[3, 3]
            return sp.Matrix([[r00, r01], [r10, r11]])
        else:
            # rho_B[i, j] = rho[i, j] + rho[i+2, j+2]
            r00 = rho[0, 0] + rho[2, 2]
            r01 = rho[0, 1] + rho[2, 3]
            r10 = rho[1, 0] + rho[3, 2]
            r11 = rho[1, 1] + rho[3, 3]
            return sp.Matrix([[r00, r01], [r10, r11]])
