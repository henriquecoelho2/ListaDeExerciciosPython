print(f'Preencha os valores corretamente')
parada= False
while parada == False:
    print(f'Seu nome')
    Nome= input()
    if len(Nome) <= 2:
        print(f'valor invalido')
    else:
        parada= True
while parada == True:
    print(f'Sua idade')
    Idade= int(input())
    if Idade <=0 and Idade >=150:
        print(f'valor invalido')
    else:
        parada= False
while parada == False:
    print (f'Seu salário')
    Salario= int(input())
    if Salario <= 0:
        print(f'Valor invalido')
    else:
        parada= True
while parada == True:
    print(f'Seu sexo (digite "m" ou "f")')
    Sexo= input()
    if Sexo != "m" or "f":
        print(f'Valor invalido')
    else:
        parada= False
while parada == False:
    print(f'Seu estado civil (s, c, v ou d)')
    EstadoCivil= input()        
    if EstadoCivil != "s" or EstadoCivil != "c" or EstadoCivil !="v" or EstadoCivil !="d":
        parada= True