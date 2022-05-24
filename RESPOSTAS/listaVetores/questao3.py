"""
Escreva um programa que leia um vetor V contendo N elementos inteiros (N será lido)
e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver, informe em que posição (índice).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K aparece.

"""
from random import randint

N = int(input("Digite um valor para N: "))
K = int(input("Digite um valor para K: "))

vetorV = [None] * N
posicaoV = []


for i in range(N):
    vetorV[i] = randint(0,30)
    if K == vetorV[i]:
       posicaoV.append(i)

print(vetorV, end=" ")
print(posicaoV, end=" ")
   
        





