diflist = []
parada = False
print (f'digite dois numeros')
primeiroNumero = int(input())
segundoNumero = int(input())
z = 0.0
x = primeiroNumero
y = segundoNumero

while parada == False:
    z = y/x
    if z > 1 :
        x += 1
        diflist.append(x)
    elif z < 1 :
        y += 1
        diflist.append(y)
    elif z == 1:
        diflist.pop ()
        parada = True
print(f'Os números entre {primeiroNumero} e {segundoNumero} são: {diflist}')