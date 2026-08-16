import sympy as sp

class GeneralRelativityEngine:
    """
    Symbolic tensor computation engine for General Relativity, Cosmology, and Gravitational Field Equations.
    Calculates Christoffel Symbols, Riemann Tensor, Ricci Tensor, Ricci Scalar, and Einstein Tensor G_{mu nu}.
    """
    def __init__(self, coordinates, metric_matrix):
        """
        :param coordinates: list of sympy symbols, e.g. [t, r, theta, phi]
        :param metric_matrix: 4x4 sympy Matrix for metric tensor g_{\mu \nu}
        """
        self.coords = coordinates
        self.dim = len(coordinates)
        self.g = metric_matrix
        self.g_inv = self.g.inv()
        
    def christoffel_symbols(self):
        """Calculates Christoffel symbols Gamma^\mu_{\alpha \beta}"""
        Gamma = [[[0 for _ in range(self.dim)] for _ in range(self.dim)] for _ in range(self.dim)]
        for k in range(self.dim):
            for i in range(self.dim):
                for j in range(self.dim):
                    res = 0
                    for m in range(self.dim):
                        t1 = sp.diff(self.g[j, m], self.coords[i])
                        t2 = sp.diff(self.g[i, m], self.coords[j])
                        t3 = sp.diff(self.g[i, j], self.coords[m])
                        res += 0.5 * self.g_inv[k, m] * (t1 + t2 - t3)
                    Gamma[k][i][j] = sp.simplify(res)
        self.Gamma = Gamma
        return Gamma

    def ricci_tensor(self):
        """Calculates Ricci curvature tensor R_{\mu \nu}"""
        if not hasattr(self, 'Gamma'):
            self.christoffel_symbols()
            
        R = sp.zeros(self.dim, self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                res = 0
                for m in range(self.dim):
                    t1 = sp.diff(self.Gamma[m][i][j], self.coords[m])
                    t2 = sp.diff(self.Gamma[m][i][m], self.coords[j])
                    
                    t3 = sum(self.Gamma[m][k][m] * self.Gamma[k][i][j] for k in range(self.dim))
                    t4 = sum(self.Gamma[m][k][j] * self.Gamma[k][i][m] for k in range(self.dim))
                        
                    res += t1 - t2 + t3 - t4
                R[i, j] = sp.simplify(res)
        self.R = R
        return R

    def ricci_scalar(self):
        """Calculates Ricci scalar R = g^{\mu \nu} R_{\mu \nu}"""
        if not hasattr(self, 'R'):
            self.ricci_tensor()
            
        scalar = sum(self.g_inv[i, j] * self.R[i, j] for i in range(self.dim) for j in range(self.dim))
        self.R_scalar = sp.simplify(scalar)
        return self.R_scalar

    def einstein_tensor(self):
        """Calculates Einstein Tensor G_{\mu \nu} = R_{\mu \nu} - (1/2) R g_{\mu \nu}"""
        if not hasattr(self, 'R_scalar'):
            self.ricci_scalar()
            
        G = sp.zeros(self.dim, self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                G[i, j] = sp.simplify(self.R[i, j] - 0.5 * self.R_scalar * self.g[i, j])
        self.G = G
        return G
