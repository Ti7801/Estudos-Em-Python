"""
Escreva um programa que:
• Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de uma turma e a média de cada um deles.
o As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
o As médias serão calculadas e armazenadas na 4ª coluna da matriz.
• Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
• Calcule e imprima a média geral da turma.
• Calcule e imprima o número de alunos com média superior à média geral da turma.
"""

notas = [[None]*4 for i in range(20)]
media_geral_turma = 0.0
alunos = 5
alunos_media_maior= 0

for i in range(alunos):
    cont = 1
    soma_notas = 0.0
    media = 0.0
    for j in range(3):
        notas[i][j] = float(input(f'Digite a {cont} nota do aluno: '))
        soma_notas = soma_notas + notas[i][j]
        cont = cont + 1 
    media = soma_notas/3
    notas[i][3] = media

    media_geral_turma = media_geral_turma + notas[i][j]

media_geral_turma = media_geral_turma/alunos    

for i in range(alunos):
        if notas[i][3] > media_geral_turma:
            alunos_media_maior = alunos_media_maior + 1 
            
                
for i in range(alunos):
    for j in range(4):
        print(f'{notas[i][j]:4}', end=" ")
    print()                    
    
print('\n')

print(f'A média geral da turma é: {media_geral_turma}')    
print(f'Número de Alunos com média superior a MÉDIA GERAL da turma: {alunos_media_maior}')
    
    