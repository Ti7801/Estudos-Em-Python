"""
Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
Ao final, exiba as 3 matrizes (no formato de matriz).
"""


matrizA = [[None] * 3 for i in range(2)]

matrizB = [[None]* 3 for i in range(2)]

matrizC = [[None]*3 for i in range(2)]


for i in range(2):
    for j in range(3):
        matrizA[i][j] = int(input("Digite um número para a matriz A: ")) 

for i in range(2):
    for j in range(3):
        matrizB[i][j] = int(input("Digite um número para a matriz B: "))        
        

for  i in range(2):
    for j in range(3):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
        
        
print(matrizC)


