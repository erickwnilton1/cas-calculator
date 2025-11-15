from algebra import *
from vetores import *
from matrizes import *
from relacoes import *

def menu():
    print("\n=== CALCULADORA ALGEBRICA FUTURISTA ===")
    print("[1] Simplificacao algebrica")
    print("[2] Derivacao")
    print("[3] Integrcao")
    print("[4] Fatoracao")
    print("[5] Resolver equacao")
    print("[6] Operacoes com vetores")
    print("[7] Operacoes com matrizes")
    print("[8] Relacoes e produto cartesiano")
    print("[0] Sair")
    return input("Escolha uma opcao: ")

def main():
    while True:
        op = menu()

        if op == "1":
            exp = input("Expressao: ")
            print("Resultado:", simplificar(exp))

        elif op == "2":
            exp = input("Expressao: ")
            print("Resultado:", derivar(exp))

        elif op == "3":
            exp = input("Expressao: ")
            print("Resultado:", integrar(exp))

        elif op == "4":
            exp = input("Expressao: ")
            print("Resultado:", fatorar(exp))

        elif op == "5":
            exp = input("Equacao (ex: 2*x+3=11): ")
            print("Resultado:", resolver_equacao(exp))

        elif op == "6":
            v1 = list(map(float, input("Vetor 1: ").split()))
            v2 = list(map(float, input("Vetor 2: ").split()))
            print("Soma:", soma_vetores(v1, v2))
            print("Produto escalar:", produto_escalar(v1, v2))
            print("Distância:", distancia(v1, v2))

        elif op == "7":
            print("Operações com matrizes... (podemos implementar tela separada)")

        elif op == "8":
            print("Produto cartesiano A x B")
            A = input("A (ex: 1,2,3): ").split(",")
            B = input("B (ex: a,b,c): ").split(",")
            print("Resultado:", produto_cartesiano(A, B))

        elif op == "0":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
