VetorDe20numeros= [2, 5, 6, 3, 4, 6, 8, 4, 67, 4657, 343, 4312, 89 ,2341 , 678, 32 ,7, 61 ,87, 2356]

Pares=[]
Impares=[]
for i in VetorDe20numeros:
    if i%2 == 0:
        Pares = i
    else:
        Impares = i
    print ('os valores pares são ' + str(Pares))
    print('os valores impares são ' + str(Impares))
