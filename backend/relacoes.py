from typing import List, Any

def produto_cartesiano(A: List[Any], B: List[Any]):
    return [(a, b) for a in A for b in B]

def eh_funcao(relacao: List[tuple]) -> bool:
    dominio = [x for x, _ in relacao]
    return len(dominio) == len(set(dominio))
