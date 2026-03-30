continuar = True


while continuar :
    print("digite o nome do aluno")
    aluno = input()
    resp = int(input('Deseja continuar : \n0 para Nao\n1 para Sim'))
    if resp == 0:
        continuar = False
    