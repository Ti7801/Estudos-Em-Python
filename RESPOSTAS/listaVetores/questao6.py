"""
Escreva um programa que leia um vetor de N números inteiros (N será lido),
inverta a ordem dos elementos do vetor e exiba o vetor invertido.
Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em ordem inversa!
"""

N = int(input("Digite um valor  para N: "))

vetorV = [None]*N
vetorA = [None]*N

for i in range(N):
    vetorV[i] = int(input("Digite um valor para o vetor: ")) 
    
for i in range(N):
    vetorA[i] = vetorV[N - 1 - i]
    
print(f"Os elementos do vetorV invertidos são: {vetorA}")

