"""
Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem
será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B
corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se
o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0
(zero).

"""
import random

N = int(input("Digite a ordem da matriz: "))

matrizA = [[None]* N for i in range(N)]

MatrizB = [[None]* N for i in range(N)]

for i in range(N):
    for j in range(N):
        matrizA[i][j] = int(random.randint(1,20))


for i in range(N):
    for j in range(N):
        if i == j:
            MatrizB[i][j] = 0
        else: 
            MatrizB[i][j] = matrizA[i][j] + i + j 

for i in range(N):
    for j in range(N):
        if i + j + 1 == N:
            MatrizB[i][j] = 0                 
  
for i in range(N):
    for j in range(N):
        print(f'{matrizA[i][j]:4}', end=" ") 
    print()                
            
print('\n\n')            
            
for i in range(N):
    for j in range(N):
        print(f'{MatrizB[i][j]:4}', end=" ") 
    print()    


