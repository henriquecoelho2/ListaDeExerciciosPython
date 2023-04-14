print(f'insira uma nota de 0-10')
parada=False

while parada == False:
    nota = input()
    if int(nota) >= 0 and int(nota) <=10:
        print('valor valido.')
        parada=True
    else:
        print('valor invalido, por favor repita.')