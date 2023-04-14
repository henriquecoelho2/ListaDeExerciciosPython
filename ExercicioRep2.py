print(f'insira seu nome e sua senha')
parada =False

while parada == False:
    Nome = input()
    Senha = input()
    if Nome == Senha:
        print(f'O nome não pode ser igual a senha, tente novamente')
    else:
        print(f'Valor válido')
        parada = True
