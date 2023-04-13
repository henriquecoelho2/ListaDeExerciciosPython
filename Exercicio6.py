alunosNotas = [['Caio', [1, 8 ,5, 3]], ['Maykon', [7, 7, 1, 7]], ['Henrique', [7, 5, 8, 3]], ['Davi', [1, 1 ,1, 1]], ['Barbosa', [4, 7, 3, 7]], ['Miguel', [5, 2, 8, 4]], ['Leticia', [6, 6, 6, 1]], ['Natalia', [10 ,10, 1 ,1]], ['Farias', [2, 3, 10, 1]], ['Ian', [2, 4, 5, 3]]]
numeroDeAlunos = 0

def calcular_media_notas(aluno):
    notas = aluno[1]
    media = sum(notas) / len(notas)
    return media

for aluno in alunosNotas:
    nome = aluno[0]
    media = calcular_media_notas(aluno)
    if media >= 5:
        numeroDeAlunos = numeroDeAlunos + 1
print(numeroDeAlunos)


