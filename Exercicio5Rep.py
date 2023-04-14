paisA=float(input('insira a população do pais A '))
paisB=float(input('insira a populaçãp do pais B '))
contador=0
taxaA=float(input('insira a taxa de crescimento do paisA '))
taxaB=float(input('insira a taxa de crescimento do paisB '))

while paisA<paisB and taxaA>taxaB:
    paisA *= taxaA
    paisB *= taxaB
    contador += 1


print(f'Demoraria {contador} anos')
