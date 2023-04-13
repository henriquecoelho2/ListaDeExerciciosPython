idade = []
altura = []
idadeInvertida = []
alturaInvertida = []

for i in range(5):
    print('Digite sua idade e sua altura:')
    idadeRecebida = input()
    alturaRecebida = input()
    idade.append(idadeRecebida)
    altura.append(alturaRecebida)

for i in range(5):
    inversaoDaIdade = idade[-1-i]
    idadeInvertida.append(inversaoDaIdade)

for i in  range(5):
    inversaoDaAltura = altura[-1-i]
    alturaInvertida.append(inversaoDaAltura)

print(f'Suas idades são: {idadeInvertida} e suas alturas são: {alturaInvertida}')