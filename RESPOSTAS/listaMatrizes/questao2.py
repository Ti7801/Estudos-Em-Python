"""
Escreva um programa que:
• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
inteiros (N será lido);
• Exiba a matriz lida (no formato de matriz);
• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.
"""

from numpy import diagonal


N = int(input("Digite a ordem da matriz: "))

matrizA = [[None]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        matrizA[i][j] = int(input('Digite um elemento para a matrizA: '))

for i in range(N):
    for j in range(N):
        print(f'{matrizA[i][j]}', end=" ")
    print()    
print('\n')

diagonal_principal = []

for i in range(N):
    for j in range(N):
        if i == j:
            diagonal_principal.append(matrizA[i][j])      
            
print(f' Os elementos da diagonal principal são : {diagonal_principal}')            