"""
Escreva um programa que leia um vetor V (contendo 30 inteiros) 
e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.
"""
import random

vetorV = [None]* 30
ocorrencia_k = 0

K = int(input("Digite um valor para K: "))

for i in range(30):
    # vetorV[i] = int(input("Digite um elemento para o vetorV: "))
    vetorV[i] = random.randint(0,10)
    if K == vetorV[i]:
        ocorrencia_k = ocorrencia_k + 1 
        
print(f"O valor de K aparece no vetor {ocorrencia_k} vezes")        

print(vetorV)

