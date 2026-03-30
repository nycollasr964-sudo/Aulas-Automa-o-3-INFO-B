

while True:
    usuario = input("digite seu login; ")
    senha = input('digite sua senha: ')

    if usuario == 'admin' and senha == 'admin123':
        print("Bem vindo ao Sistema")
        break
    else :
        print('Usuario ou senha invalido')