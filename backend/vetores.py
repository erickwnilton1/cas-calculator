import numpy as np
from typing import List

def soma_vetores(v1: List[float], v2: List[float]) -> List[float]:
    return (np.array(v1, dtype=float) + np.array(v2, dtype=float)).tolist()

def produto_escalar(v1: List[float], v2: List[float]) -> float:
    return float(np.dot(np.array(v1, dtype=float), np.array(v2, dtype=float)))

def distancia(v1: List[float], v2: List[float]) -> float:
    return float(np.linalg.norm(np.array(v1, dtype=float) - np.array(v2, dtype=float)))
