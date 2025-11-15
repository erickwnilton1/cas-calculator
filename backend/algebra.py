import sympy as sp

def simplificar(expressao: str):
    """
    Simplifica expressoes algebricas usando SymPy.
    Exemplo: '2x + 4x - 3' -> '6x - 3'
    """
    x = sp.symbols("x")
    return sp.simplify(expressao)


def derivar(expressao: str, variavel: str = 'x'):
    """
    Deriva uma expressao algebrica.
    """
    var = sp.symbols(variavel)
    return sp.diff(expressao, var)


def integrar(expressao: str, variavel: str = 'x'):
    """
    Integra uma expressao algebrica.
    """
    var = sp.symbols(variavel)
    return sp.integrate(expressao, var)


def fatorar(expressao: str):
    """
    Fatora expressoes algebricas e polinomios.
    """
    x = sp.symbols("x")
    return sp.factor(expressao)


def resolver_equacao(expressao: str):
    """
    Resolve equacoes algebricas.
    Exemplo: '2*x + 5 = 11'
    """
    x = sp.symbols("x")
    eq = sp.Eq(eval(expressao.split('=')[0]), eval(expressao.split('=')[1]))
    return sp.solve(eq, x)
