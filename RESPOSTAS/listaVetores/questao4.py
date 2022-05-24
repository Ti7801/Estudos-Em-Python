"""
4. Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.
"""

N = 5

vetorV = [None] * N
vetorPar = [None] * N
vetorImpar = [None] * N

for i in range(N):
    vetorV[i] = int(input("Digite um elemento: ")) 
    if (i%2) == 0:
       vetorPar[i] = vetorV[i]
    else:
        vetorImpar[i] = vetorV[i]
        
print(f"Números com indices Pares : {vetorPar}\n")
print(f"Números com indices Impares: {vetorImpar}")        
     

    
    
    