import numpy as np

def multiplicar_matrizes(A, B):
    return np.matmul(A, B)

def determinante(A):
    return np.linalg.det(A)

def resolver_sistema(A, b):
    """
    Resolve Ax = b
    """
    return np.linalg.solve(A, b)

def autovalores_autovetores(A):
    return np.linalg.eig(A)
