vetorA = ['1', '2' ,'3', '4' ,'5' ,'6', '7', '8', '9', '10']
vetorDosQuadrados =[]

for i in vetorA:
    quadradosDosNumerosNaturaisDoVetorA = int(i)**2
    vetorDosQuadrados.append(quadradosDosNumerosNaturaisDoVetorA)



print (f'os quadrados dos números são {vetorDosQuadrados} e a soma é:{sum(vetorDosQuadrados)}')