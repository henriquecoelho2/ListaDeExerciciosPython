lista1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2=[]

for i in range(0, 10):
    varPop = lista1.pop()
    lista2.append(varPop)

print(lista2)