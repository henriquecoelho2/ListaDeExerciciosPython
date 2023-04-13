vetorUnico = [[1, 3], [2, 4], [3, 7], [4, 2], [5, 6], [6, 9], [7, 1], [8, 1], [9, 2] ,[10, 3]]
somaDosVetores = []
for i in vetorUnico:
    primeiroVetor = i[0]
    segundoVetor = i[1]
    somaDosVetores.append(primeiroVetor + segundoVetor)

print(somaDosVetores)