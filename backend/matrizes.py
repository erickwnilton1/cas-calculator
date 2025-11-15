import numpy as np
from typing import List, Optional, Tuple

def multiplicar_matrizes(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    return (np.array(A, dtype=float) @ np.array(B, dtype=float)).tolist()

def determinante(A: List[List[float]]) -> float:
    return float(np.linalg.det(np.array(A, dtype=float)))

def resolver_sistema(A: List[List[float]], b: List[float]) -> List[float]:
    sol = np.linalg.solve(np.array(A, dtype=float), np.array(b, dtype=float))
    return sol.tolist()

def autovalores_autovetores(A: List[List[float]]) -> Tuple[List[float], List[List[float]]]:
    vals, vecs = np.linalg.eig(np.array(A, dtype=float))
    return vals.tolist(), vecs.tolist()
