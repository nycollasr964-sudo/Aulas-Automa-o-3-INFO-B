n1 = float(input('Nota 1 do aluno '))
n2 = float(input('Nota 2 do aluno '))
media = (n1 + n2) /2
if media >=6:
    print('Aprovado')
else :
    exame = float(input("Digite nota do exame final"))
    nova_media = (exame + media) /2
    if nova_media >= 6:
        print("aprovado")
    else :
        print('Reprovado')



