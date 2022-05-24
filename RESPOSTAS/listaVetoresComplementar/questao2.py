"""
2. Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão lidos), 
gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a intercalação dos elementos de A e B.
Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]
"""
N = int(input("Digite um valor para N:"))

vetorA = [None]*N
vetorB = [None]*N
vetorC = [None]*2*N

for i in range(N):
    vetorA[i] = int(input("Digite um elemento para o vetor A: "))
    vetorC[i] = vetorA[i]

tamanho_A = len(vetorA)
tamanho_C = len(vetorC)
    
for i in range(N):
    vetorB[i] = int(input("Digite um elemento para o vetor B: "))
    
print(tamanho_A)
print(tamanho_C)

for i in range(tamanho_A, tamanho_C):
    vetorC[i] = vetorB[i-N]    
    


print(f"O vetor C é: {vetorC}") 
