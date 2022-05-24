"""
1. Escreva um programa que leia um vetor contendo N elementos inteiros (N será lido), calcule e exiba:
• A quantidade de elementos pares;
• A quantidade de elementos ímpares;
• A soma de todos os elementos;
• A média dos elementos do vetor.

"""
N = int(input("Digite um valor para N: "))

pares = 0
impares = 0
vetorV = [None]*N
soma=0
media=0

for i in range(N):
    vetorV[i]= int(input("Digite um valor para o vetor:"))
    soma = soma + vetorV[i]
    
media = soma/N    

for i in range(N):
    if vetorV[i]%2==0: 
        pares = pares + 1
    else:
        impares = impares + 1       

print(f'A quantidade de elementos pares é: {pares}')
print(f'A quantidade de elementos impares é: {impares}')
print(f'A soma dos elementos do vetor é: {soma}')
print(f'A média dos elementos do vetor é: {media}')
        