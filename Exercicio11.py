vetorPrimeiro = list(range (10))
vetorSegundo = list(range (9, -1, -1))
vetorTerceiro= list(range (11, 21))
vetorQuarto = []

for i in range(10):
    vetorTemporario = vetorPrimeiro[i]
    vetorQuarto.append(vetorTemporario)
    vetorTemporario = vetorSegundo [i]
    vetorQuarto.append(vetorTemporario)
    vetorTemporario = vetorTerceiro [i]
    vetorQuarto.append (vetorTemporario)

print (vetorPrimeiro)
print (vetorSegundo)
print (vetorTerceiro)
print (vetorQuarto)