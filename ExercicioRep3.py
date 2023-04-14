sexos=['f', 'm']
estadosCivis=['s', 'v' ,'d', 'c']

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
    sexo = input('Digite seu sexo "m" ou "f"')
    if sexo in sexos:
        print(f'Vc colocou {sexo}')
        parada = False
    else:
        print('errou')
while parada == False:
    print(f'Seu estado civil (s, c, v ou d)')
    EstadoCivil= input()        
    if EstadoCivil in estadosCivis:
        parada= True
    else:
        print(f'Valor invalido')