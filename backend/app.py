from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Any, Optional
from fastapi.middleware.cors import CORSMiddleware

from . import algebra
from . import vetores
from . import matrizes
from . import relacoes

app = FastAPI(title="CAS Calculator API", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ExprIn(BaseModel):
    expr: str
    variable: Optional[str] = "x"

class EquationIn(BaseModel):
    equation: str
    variable: Optional[str] = "x"

class VectorIn(BaseModel):
    v1: List[float]
    v2: List[float]

class MatrixIn(BaseModel):
    A: List[List[float]]
    B: Optional[List[List[float]]] = None
    b: Optional[List[float]] = None

class CartesianIn(BaseModel):
    A: List[Any]
    B: List[Any]

@app.get("/")
def root():
    return {"message": "CAS Calculator API running"}

# ALGEBRA
@app.post("/algebra/simplify")
def api_simplify(payload: ExprIn):
    try:
        return {"result": algebra.simplificar(payload.expr)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/algebra/diff")
def api_diff(payload: ExprIn):
    try:
        return {"result": algebra.derivar(payload.expr, payload.variable)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/algebra/integrate")
def api_integrate(payload: ExprIn):
    try:
        return {"result": algebra.integrar(payload.expr, payload.variable)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/algebra/factor")
def api_factor(payload: ExprIn):
    try:
        return {"result": algebra.fatorar(payload.expr)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/algebra/solve")
def api_solve(payload: EquationIn):
    try:
        return {"result": algebra.resolver_equacao(payload.equation, payload.variable)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# VECTOR
@app.post("/vector/sum")
def api_vector_sum(payload: VectorIn):
    try:
        return {"result": vetores.soma_vetores(payload.v1, payload.v2)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/vector/dot")
def api_vector_dot(payload: VectorIn):
    try:
        return {"result": vetores.produto_escalar(payload.v1, payload.v2)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/vector/dist")
def api_vector_dist(payload: VectorIn):
    try:
        return {"result": vetores.distancia(payload.v1, payload.v2)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# MATRIX
@app.post("/matrix/multiply")
def api_matrix_multiply(payload: MatrixIn):
    try:
        if payload.B is None:
            raise ValueError("Campo B obrigatório para multiplicação")
        return {"result": matrizes.multiplicar_matrizes(payload.A, payload.B)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/matrix/det")
def api_matrix_det(payload: MatrixIn):
    try:
        return {"result": matrizes.determinante(payload.A)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/matrix/solve")
def api_matrix_solve(payload: MatrixIn):
    try:
        if payload.b is None:
            raise ValueError("Campo b obrigatório para resolver sistema")
        return {"result": matrizes.resolver_sistema(payload.A, payload.b)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/matrix/eigen")
def api_matrix_eigen(payload: MatrixIn):
    try:
        vals, vecs = matrizes.autovalores_autovetores(payload.A)
        return {"eigenvalues": vals, "eigenvectors": vecs}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# RELATIONS
@app.post("/relations/cartesian")
def api_cartesian(payload: CartesianIn):
    try:
        return {"result": relacoes.produto_cartesiano(payload.A, payload.B)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
