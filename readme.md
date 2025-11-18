# **CAS Calculator**

A **CAS Calculator** é uma aplicação desenvolvida para demonstrar, de forma prática, os conceitos fundamentais da disciplina de **Estruturas Matemáticas**. <br />
A API implementa operações algébricas, vetoriais, matriciais e manipulação de relações matemáticas utilizando **Python**, **FastAPI**, **SymPy** e **NumPy**, **Html**, **Css**, **JavaScript**.

---

### 1. Stack Utilizada

- [ ] Python 3.12
- [ ] FastAPI
- [ ] Uvicorn
- [ ] SymPy
- [ ] NumPy
- [ ] Html
- [ ] Css
- [ ] JavaScript

---

### 2. Estrutura do Projeto

```
cas-calculator/
│
├── backend/
│   ├── app.py             # Arquivo principal da API
│   ├── algebra.py         # Operações algébricas (SymPy)
│   ├── vetores.py         # Operações vetoriais (NumPy)
│   ├── matrizes.py        # Operações com matrizes
│   ├── relacoes.py        # Conjuntos e produto cartesiano
|
├── index.html
├── style.css
├── script.js
│
└── readme.md              # Documentação
```

---

### 3. Instalação do Ambiente

### 3.1. Clonar o repositório

```bash
git clone https://github.com/erickwnilton1/cas-calculator
cd cas-calculator
```

### 3.2. Criar ambiente virtual

```bash
python -m venv venv
```

Ativação:

- Windows:

  ```bash
  venv\Scripts\activate
  ```

- Linux/Mac:

  ```bash
  source venv/bin/activate
  ```

### 3.3. Instalar dependências

```bash
pip install fastapi uvicorn sympy numpy
```

---

### 4. Como executar:

No diretório raiz do projeto:

```bash
python -m uvicorn backend.app:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

Executar Frontend:

```
index.html
```

em qualquer navegador.

---

### 5. Documentação automática (Swagger UI)

Acesse:

```
http://127.0.0.1:8000/docs
```

---

### 6. Endpoints da API

### 6.1 Álgebra Simbólica

Arquivo: `algebra.py`

| Método | Rota                 | Descrição               |
| ------ | -------------------- | ----------------------- |
| POST   | `/algebra/simplify`  | Simplificação algébrica |
| POST   | `/algebra/diff`      | Derivação               |
| POST   | `/algebra/integrate` | Integração              |
| POST   | `/algebra/factor`    | Fatoração               |
| POST   | `/algebra/solve`     | Resolver equações       |

#### Exemplo:

```json
{
  "expr": "2*x + 3*x"
}
```

---

### 6.2 Operações com Vetores

Arquivo: `vetores.py`

| Método | Rota           | Descrição                |
| ------ | -------------- | ------------------------ |
| POST   | `/vector/sum`  | Somar dois vetores       |
| POST   | `/vector/dot`  | Calcular produto escalar |
| POST   | `/vector/dist` | Distância entre vetores  |

---

### 6.3 Relações e Produto Cartesiano

Arquivo: `relacoes.py`

| Método | Rota                   | Descrição  |
| ------ | ---------------------- | ---------- |
| POST   | `/relations/cartesian` | Gera A × B |

---

### 7. Testes

A API pode ser testada de três formas:

1. **Swagger UI** (recomendado)
   `http://127.0.0.1:8000/docs`

2. **Thunder Client** (VS Code)

3. **Postman**
