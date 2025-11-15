from itertools import product

def produto_cartesiano(A, B):
    return list(product(A, B))

def verificar_funcao(relacao):
    """
    Verifica se uma relacao e funcao.
    Relacao = [(x, y), ...]
    """
    dominio = [x for x, _ in relacao]
    return len(dominio) == len(set(dominio))
