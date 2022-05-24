"""
Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma
dada matriz.
Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada
por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].

Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as
duas matrizes (no formato de matriz).

"""

import random


MatrizA = [[None]*5 for i in range(3)]

for i in range(3):
    for j in range(5):
        MatrizA[i][j] = random.randint(1,50)



for i in range(3):
    for j in range(5):
        print(f'{MatrizA[i][j]:4}', end=" ")
    print()    
    
  
print('\n')
for i in range(5):
    for j in range(3):
        print(f'{MatrizA[j][i]:4}', end=" ")
    print()    
        
   
        
        