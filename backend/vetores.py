import numpy as np

def soma_vetores(v1, v2):
    return np.add(v1, v2)

def produto_escalar(v1, v2):
    return np.dot(v1, v2)

def norma(v):
    return np.linalg.norm(v)

def distancia(v1, v2):
    return np.linalg.norm(np.array(v1) - np.array(v2))
