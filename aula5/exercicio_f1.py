def quadrado (n1):
    return n1 ^ 2
def imprimir(texto):
    print(texto)

def ler():
    return int(input())

def pulaLinha():
    print('\n')


imprimir('Digite o número 1')
n1 = ler()


resposta = quadrado(n1)
imprimir(f'O resultado é {resposta}')