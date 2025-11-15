import sympy as sp
from typing import Optional

def simplificar(expr_str: str) -> str:
    expr = sp.sympify(expr_str)
    return str(sp.simplify(expr))

def expandir(expr_str: str) -> str:
    expr = sp.sympify(expr_str)
    return str(sp.expand(expr))

def fatorar(expr_str: str) -> str:
    expr = sp.sympify(expr_str)
    return str(sp.factor(expr))

def derivar(expr_str: str, var: Optional[str] = "x") -> str:
    var_sym = sp.symbols(var)
    expr = sp.sympify(expr_str)
    return str(sp.diff(expr, var_sym))

def integrar(expr_str: str, var: Optional[str] = "x") -> str:
    var_sym = sp.symbols(var)
    expr = sp.sympify(expr_str)
    return str(sp.integrate(expr, var_sym))

def resolver_equacao(eq_str: str, var: Optional[str] = "x"):
    if "=" in eq_str:
        lhs, rhs = eq_str.split("=", 1)
        sol = sp.solve(sp.Eq(sp.sympify(lhs), sp.sympify(rhs)), sp.symbols(var))
    else:
        sol = sp.solve(sp.sympify(eq_str), sp.symbols(var))
    return [str(s) for s in sol]
