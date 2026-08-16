import sympy as sp

class InformationTheoryEngine:
    """
    Symbolic evaluation engine for Classical Information Theory,
    Shannon Entropy, KL Divergence, Mutual Information, and Fisher Information.
    """
    def shannon_entropy(self, probabilities, base=2):
        """Calculates Shannon entropy H(P) = -sum(p * log(p))"""
        H = 0
        for p in probabilities:
            if p > 0:
                if base == 2:
                    H -= p * sp.log(p, 2)
                else:
                    H -= p * sp.log(p)
        return sp.simplify(H)

    def kl_divergence(self, P, Q, base=2):
        """Calculates Kullback-Leibler divergence D_KL(P || Q)"""
        d_kl = 0
        for p, q in zip(P, Q):
            if p > 0 and q > 0:
                if base == 2:
                    d_kl += p * sp.log(p / q, 2)
                else:
                    d_kl += p * sp.log(p / q)
        return sp.simplify(d_kl)

    def fisher_information_1d(self, log_p_func, theta_symbol, x_symbol):
        """
        Computes 1D Fisher Information I(theta) = - E[ d^2/dtheta^2 ln p(x; theta) ]
        :param log_p_func: sympy expression for ln p(x; theta)
        """
        d2_log_p = sp.diff(log_p_func, theta_symbol, 2)
        return sp.simplify(-d2_log_p)
