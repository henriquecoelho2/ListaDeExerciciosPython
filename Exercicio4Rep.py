paisA=80000
paisB=200000
contador=0

while paisA<paisB:
    paisA *= 1.03
    paisB *= 1.015
    contador += 1

print(f'Demoraria {contador} anos')
