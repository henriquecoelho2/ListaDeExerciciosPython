vetorDeNumerosInteiros=[29, 42, 62, 56 ,3]
soma = sum(vetorDeNumerosInteiros)
multiplicação = vetorDeNumerosInteiros[0]
for i in vetorDeNumerosInteiros[1:5]:
    multiplicação = i * multiplicação
print(f'os números são: {vetorDeNumerosInteiros} a soma dos números é {soma} e a multiplicação é {multiplicação}')