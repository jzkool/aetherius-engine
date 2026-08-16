import sympy as sp

class GeometryProver:
    """
    A helper class to automate symbolic differential geometry proofs.
    Computes Christoffel symbols, Riemann curvature, Ricci tensor, and Ricci scalar.
    """
    def __init__(self, coordinates, metric_matrix):
        """
        :param coordinates: list of sympy symbols, e.g., [x, y, z]
        :param metric_matrix: sympy Matrix representing g_{ij}
        """
        self.coords = coordinates
        self.dim = len(coordinates)
        self.g = metric_matrix
        self.g_inv = self.g.inv()
        
    def christoffel_symbols(self):
        """
        Computes Christoffel symbols of the second kind: Gamma^k_{ij}
        Returns a list of lists of lists.
        """
        Gamma = [[[0 for _ in range(self.dim)] for _ in range(self.dim)] for _ in range(self.dim)]
        for k in range(self.dim):
            for i in range(self.dim):
                for j in range(self.dim):
                    res = 0
                    for m in range(self.dim):
                        term1 = sp.diff(self.g[j, m], self.coords[i])
                        term2 = sp.diff(self.g[i, m], self.coords[j])
                        term3 = sp.diff(self.g[i, j], self.coords[m])
                        res += 0.5 * self.g_inv[k, m] * (term1 + term2 - term3)
                    Gamma[k][i][j] = sp.simplify(res)
        self.Gamma = Gamma
        return Gamma

    def ricci_tensor(self):
        """
        Computes the Ricci tensor R_{ij}
        Returns a sympy Matrix.
        """
        if not hasattr(self, 'Gamma'):
            self.christoffel_symbols()
            
        R = sp.zeros(self.dim, self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                res = 0
                for m in range(self.dim):
                    t1 = sp.diff(self.Gamma[m][i][j], self.coords[m])
                    t2 = sp.diff(self.Gamma[m][i][m], self.coords[j])
                    
                    t3 = 0
                    for k in range(self.dim):
                        t3 += self.Gamma[m][k][m] * self.Gamma[k][i][j]
                        
                    t4 = 0
                    for k in range(self.dim):
                        t4 += self.Gamma[m][k][j] * self.Gamma[k][i][m]
                        
                    res += t1 - t2 + t3 - t4
                R[i, j] = sp.simplify(res)
        self.R = R
        return R

    def ricci_scalar(self):
        """
        Computes the Ricci scalar R = g^{ij} R_{ij}
        """
        if not hasattr(self, 'R'):
            self.ricci_tensor()
            
        scalar = 0
        for i in range(self.dim):
            for j in range(self.dim):
                scalar += self.g_inv[i, j] * self.R[i, j]
                
        return sp.simplify(scalar)

    def print_christoffel(self):
        if not hasattr(self, 'Gamma'):
            self.christoffel_symbols()
        for k in range(self.dim):
            for i in range(self.dim):
                for j in range(self.dim):
                    val = self.Gamma[k][i][j]
                    if val != 0:
                        print(f"Gamma^{self.coords[k]}_{self.coords[i]}{self.coords[j]} = {val}")

