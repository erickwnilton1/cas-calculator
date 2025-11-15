## Cas-calculator

Computador Algébrico

A CAS Calculator é uma aplicação desenvolvida para demonstrar, de forma prática, os conceitos fundamentais da disciplina de Estruturas Matemáticas.
O sistema reúne operações algébricas, vetoriais, matriciais e manipulação de relações matemáticas em um ambiente totalmente executado via terminal.

---

### 🧠 Funcionalidades

🔢 1. Álgebra Simbólica (SymPy)

- [ ] Simplificação algébrica
- [ ] Derivação
- [ ] Integração
- [ ] Fatoração
- [ ] Resolução de equações

🧭 2. Operações com Vetores (NumPy)

- [ ] Soma de vetores
- [ ] Produto escalar
- [ ] Distância entre vetores

🟦 3. Operações com Matrizes

- [ ] Soma de matrizes (opcional expandir)
- [ ] Multiplicação por escalar
- [ ] Multiplicação matricial

🔗 4. Relações e Produto Cartesiano

- [ ] Representação de conjuntos
- [ ] Geração do produto cartesiano
- [ ] Manipulação básica de relações

🛰️ 5. Interface Futurista no Terminal

- [ ] Menu interativo
- [ ] Organização clara das opções
- [ ] Execução totalmente via terminal

---

### Tecnologias utilizadas

- [ ] Python 3.12
- [ ] SymPy
- [ ] NumPy
- [ ] Terminal (CLI)

---

### Como executar:

Clonar o repositório:

```bash
git clone https://github.com/erickwnilton1/cas-calculator
cd cas-calculator
```

(Projeto recomendado com ambiente virtual)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

Instalar dependências:

```bash
pip install numpy
```

Executar a aplicação:

```bash
python main.py
```

---

### Estrutura do projeto

```
/cas-calculator
|- Backend
│── main.py          # menu principal
│── algebra.py       # operações simbólicas
│── vetores.py       # operações com vetores
│── matrizes.py      # operações com matrizes
│── relacoes.py      # conjunto e produto cartesiano
│── readme.md        # documentação
```
