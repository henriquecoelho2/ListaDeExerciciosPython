VetorDe10Caracteres= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numeroDeconsoantes = 0
Vogais=['a', 'e' , 'i', 'o' ,   'u']
for i in VetorDe10Caracteres:
    if i not in Vogais:
        numeroDeconsoantes = numeroDeconsoantes + 1
        print(i)
print (numeroDeconsoantes)