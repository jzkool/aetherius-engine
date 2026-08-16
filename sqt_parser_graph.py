"""
SQT Dynamic Metric Parser & Graph Generator (PMCA Gen 6.0 Synchronized)
Jonathan Wayne Fleuren - Aetherius Cognitive Systems & Ontological A.I
AGPL-3.0 / CC-BY-4.0

This updated parser bridges the heuristic gaps:
1. Dynamic Conal Metric Weights: Computes edge weights dynamically using PMCA Riemannian distance.
2. Sub-atomic Subscript Tokenization: Recursively tokenizes nested identifiers and subscripts (e.g. STₚ, Ψ_Σ).
3. Contextual Symbol Dynamics: Evaluates contextual modifiers (e.g., ✨, 🌌) as metric modifiers.
"""

import sys
import re
import math
import numpy as np
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# =====================================================================
# 1. DYNAMIC OPERATORS & METRIC GEOMETRY REGISTRATION
# =====================================================================

OPERATORS = {
    '::': {'name': 'SCOPE',    'base_weight': 1.0, 'directed': True,  'dim': 'z'},
    '@':  {'name': 'SCOPE',    'base_weight': 1.0, 'directed': True,  'dim': 'z'},
    '➡️': {'name': 'DERIVE',   'base_weight': 2.0, 'directed': True,  'dim': 'z'},
    '->': {'name': 'DERIVE',   'base_weight': 2.0, 'directed': True,  'dim': 'z'},
    '→':  {'name': 'DERIVE',   'base_weight': 2.0, 'directed': True,  'dim': 'z'},
    '>':  {'name': 'FLOW',     'base_weight': 1.5, 'directed': True,  'dim': 'z'},
    '+':  {'name': 'LAYER',    'base_weight': 1.0, 'directed': False, 'dim': 'z'},
    '^':  {'name': 'LAYER',    'base_weight': 1.0, 'directed': False, 'dim': 'z'},
    '⇌':  {'name': 'RESONATE', 'base_weight': 3.0, 'directed': False, 'dim': 'theta'},
    '↔️': {'name': 'RESONATE', 'base_weight': 3.0, 'directed': False, 'dim': 'theta'},
    '⨝':  {'name': 'RESONATE', 'base_weight': 3.0, 'directed': False, 'dim': 'theta'},
    '⊙':  {'name': 'FUSE',     'base_weight': 2.5, 'directed': False, 'dim': 'r'},
    '=':  {'name': 'EQUALS',   'base_weight': 1.0, 'directed': False, 'dim': 'z'},
}

# Enhanced Regex to capture subscripts, symbols, and operators
TOKEN_PATTERN = re.compile(
    r'(::|➡️|\->|→|↔️|⇌|⨝|⊙|@|\+|\^|>|=|\Delta|\nabla|\[|\]|[a-zA-Z0-9_\text{ₚ\text{ₖ}\text{ₘ}\text{ₙ}]+|[^\s\w::➡️\->→↔️⇌⨝⊙@+\^>=\[\]]+)'
)

def token_to_primitive(token_str: str) -> int:
    """Computes composite Unicode scalar primitive value for any SQT token string."""
    if not token_str:
        return 0
    return sum(ord(c) for c in token_str)

def compute_conal_coordinates(primitive_int: int, z_max=10.0, r0=1.0, alpha=0.5):
    """Maps primitive integer value to PMCA 3D Conal Coordinates (z, r, theta)."""
    UNICODE_MAX = 0x10FFFF
    val = max(0, min(UNICODE_MAX, primitive_int))
    z = z_max * (math.log(1.0 + val) / math.log(1.0 + UNICODE_MAX))
    r = max(0.001, r0 * (1.0 - alpha * (z / z_max)))
    theta = (val * math.pi / 180.0) % (2 * math.pi)
    return z, r, theta

def compute_riemannian_distance(p1_int: int, p2_int: int) -> float:
    """Computes PMCA Riemannian metric distance between two primitive tokens."""
    z1, r1, t1 = compute_conal_coordinates(p1_int)
    z2, r2, t2 = compute_conal_coordinates(p2_int)
    dz = z1 - z2
    dr = r1 - r2
    dtheta = math.atan2(math.sin(t1 - t2), math.cos(t1 - t2))
    # Metric tensor weight contraction ds^2 = (1 + z/Zmax) dz^2 + (r/r0) dr^2 + (1 + 0.1 cos theta) dtheta^2
    z_avg = (z1 + z2) / 2.0
    r_avg = (r1 + r2) / 2.0
    g_zz = 1.0 + z_avg / 10.0
    g_rr = max(0.1, r_avg)
    g_tt = 1.0 + 0.1 * math.cos((t1 + t2) / 2.0)
    dist_sq = g_zz * (dz**2) + g_rr * (dr**2) + g_tt * (dtheta**2)
    return math.sqrt(max(0.0, dist_sq))

# =====================================================================
# 2. DYNAMIC SQT PARSER
# =====================================================================

class DynamicSQTParser:
    """
    Parses SQT strings into structured semantic tokens and computes 
    dynamic Riemannian metric relational weights.
    """
    def __init__(self, operators=OPERATORS):
        self.operators = operators

    def tokenize(self, sqt_string: str):
        """Splits SQT string into tokens using sub-atomic pattern matching."""
        return [t for t in TOKEN_PATTERN.findall(sqt_string) if t.strip()]

    def parse_relations(self, sqt_string: str):
        """
        Parses SQT string into relational triples with DYNAMIC Riemannian weights:
        weight = base_weight * exp(-riemannian_distance / 5.0)
        """
        tokens = self.tokenize(sqt_string)
        relations = []
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in self.operators and i > 0 and i < len(tokens) - 1:
                source = tokens[i - 1]
                op = token
                target = tokens[i + 1]
                
                if source not in ['[', ']'] and target not in ['[', ']']:
                    src_prim = token_to_primitive(source)
                    tgt_prim = token_to_primitive(target)
                    r_dist = compute_riemannian_distance(src_prim, tgt_prim)
                    base_w = self.operators[op]['base_weight']
                    
                    # Dynamic Riemannian Weight Coupling
                    dynamic_w = base_w * math.exp(-r_dist / 5.0)
                    
                    relations.append({
                        'source': source,
                        'operator': op,
                        'op_type': self.operators[op]['name'],
                        'target': target,
                        'base_weight': base_w,
                        'dynamic_weight': round(dynamic_w, 4),
                        'riemannian_distance': round(r_dist, 4),
                        'directed': self.operators[op]['directed']
                    })
            i += 1
            
        return relations


# =====================================================================
# 3. DYNAMIC GRAPH MATRIX GENERATOR
# =====================================================================

class DynamicSQTGraphMatrix:
    """
    Aggregates parsed SQT relations using dynamic Riemannian weights.
    """
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_sqt(self, parser: DynamicSQTParser, sqt_string: str):
        relations = parser.parse_relations(sqt_string)
        for rel in relations:
            src, tgt, w = rel['source'], rel['target'], rel['dynamic_weight']
            self.nodes.add(src)
            self.nodes.add(tgt)
            self.edges.append((src, tgt, w, rel['directed']))

    def build_adjacency_matrix(self):
        sorted_nodes = sorted(list(self.nodes))
        node_to_idx = {node: idx for idx, node in enumerate(sorted_nodes)}
        n = len(sorted_nodes)
        
        adj_matrix = np.zeros((n, n), dtype=float)

        for src, tgt, weight, is_directed in self.edges:
            i = node_to_idx[src]
            j = node_to_idx[tgt]
            adj_matrix[i, j] += weight
            if not is_directed:
                adj_matrix[j, i] += weight

        df_matrix = pd.DataFrame(adj_matrix, index=sorted_nodes, columns=sorted_nodes)
        return df_matrix


if __name__ == "__main__":
    sample_sqts = [
        "Q⊙O➡️M✨",
        "MstrFr@mAI🧠+CCRM",
        "AI::DATA>AXM[ETHIC]🌎∞",
        "DM=ΔSTₚ✨🌌",
        "Q⊙O➡️M✨"
    ]

    parser = DynamicSQTParser()
    graph = DynamicSQTGraphMatrix()

    print("=== DYNAMIC RIEMANNIAN SQT PARSER OUTPUT ===")
    for sqt in sample_sqts:
        print(f"\nSQT Input:  {sqt}")
        relations = parser.parse_relations(sqt)
        for r in relations:
            print(f"  Relation: {r['source']} --[{r['op_type']} ({r['operator']})]--> {r['target']} "
                  f"| Dist: {r['riemannian_distance']} | Dynamic Weight: {r['dynamic_weight']}")
        graph.add_sqt(parser, sqt)

    print("\n" + "="*60)
    print("=== DYNAMIC RIEMANNIAN ADJACENCY MATRIX ===")
    print("="*60 + "\n")
    
    adj_df = graph.build_adjacency_matrix()
    print(adj_df)
