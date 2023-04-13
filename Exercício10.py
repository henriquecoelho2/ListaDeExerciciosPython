vetorPrimeiro = [1 ,2, 3, 4, 5, 6, 7 ,8, 9, 10]
vetorsegundo = [10 ,9, 8 ,7, 6, 5, 4, 3, 2 ,1]
vetorTerceiro= []
for i in range(10):
    vetorTemporario = vetorPrimeiro[i]
    vetorTerceiro.append(vetorTemporario)
    vetorTemporario = vetorsegundo [i]
    vetorTerceiro.append(vetorTemporario)
print (vetorTerceiro)
