"""
Escreva um programa que receba um vetor V de N números inteiros (N será lido), 
determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices.
Obs: suponha a inexistência de valores repetidos.
"""

N = int(input("Digite um valor para N: "))

vetorV = [None] * N

for i in range(N):
    vetorV[i] = int(input("Digite um número inteiro: "))
    
aux = vetorV[0]   

for i in range(1,N):
    if aux > vetorV[i]:
        maior = aux
    else:
        maior = vetorV[i]
    if aux < vetorV[i]:
        menor = aux
    else:
        menor = vetorV[i]        
        

print(f"O maior valor é : {maior}") 
print(f"O menor valor é : {menor}")  

