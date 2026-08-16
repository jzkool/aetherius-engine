import sympy as sp
from sympy.physics.matrices import msigma, mgamma

class QFTAlgebraEngine:
    """
    Symbolic helper engine for Quantum Field Theory (QFT), Dirac Gamma algebra,
    Pauli spin matrices, Gell-Mann QCD matrices, and gauge group commutators.
    """
    def __init__(self):
        # Dirac Gamma Matrices in Standard Representation
        self.gamma0 = mgamma(0)
        self.gamma1 = mgamma(1)
        self.gamma2 = mgamma(2)
        self.gamma3 = mgamma(3)
        self.gamma5 = mgamma(5)
        
        # Pauli Matrices for SU(2)
        self.sigma1 = msigma(1)
        self.sigma2 = msigma(2)
        self.sigma3 = msigma(3)

    def pauli_commutator(self, i, j):
        """Computes commutator [sigma_i, sigma_j] = 2i epsilon_{ijk} sigma_k"""
        s_map = {1: self.sigma1, 2: self.sigma2, 3: self.sigma3}
        A, B = s_map[i], s_map[j]
        return A * B - B * A

    def dirac_trace_4gamma(self, mu, nu, rho, sigma):
        """
        Computes Tr(gamma^mu gamma^nu gamma^rho gamma^sigma)
        Using Minkowski metric signature (-1, 1, 1, 1) or (+1, -1, -1, -1)
        """
        g_map = {0: self.gamma0, 1: self.gamma1, 2: self.gamma2, 3: self.gamma3}
        prod = g_map[mu] * g_map[nu] * g_map[rho] * g_map[sigma]
        return prod.trace()

    def get_gell_mann_matrices(self):
        """Returns the 8 Gell-Mann matrices for SU(3) QCD gauge symmetry"""
        i = sp.I
        l1 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
        l2 = sp.Matrix([[0, -i, 0], [i, 0, 0], [0, 0, 0]])
        l3 = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
        l4 = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
        l5 = sp.Matrix([[0, 0, -i], [0, 0, 0], [i, 0, 0]])
        l6 = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
        l7 = sp.Matrix([[0, 0, 0], [0, 0, -i], [0, i, 0]])
        l8 = (1 / sp.sqrt(3)) * sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])
        return [l1, l2, l3, l4, l5, l6, l7, l8]

    def gellmann_commutator(self, a, b):
        """Computes commutator [lambda_a, lambda_b] for SU(3) generators (1-indexed)"""
        gm = self.get_gell_mann_matrices()
        A, B = gm[a-1], gm[b-1]
        return sp.simplify(A * B - B * A)
