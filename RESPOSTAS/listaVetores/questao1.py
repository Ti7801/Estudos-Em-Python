"""Escreva um programa que leia um vetor A de N números inteiros (N será lido) e um outro inteiro K, 
construa e exiba um outro vetor B cujos elementos são os respectivos elementos de a multiplicados por K.
Ex: A = [1,2,3], K = 5, B = [5,10,15].
"""

N = int(input("Digite quantos elementos haverá no vetor: "))
K = int(input("Digite um valor para k: "))

vetorA = [None] * N

vetorB = [None] * N

for i in range(N):
    vetorA[i] = int(input("Digite um valor para o vetor A: ")) 
    vetorB[i] = vetorA[i] * K

print("Os elementos do vetor B são: ",vetorB)


