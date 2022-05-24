"""
Escreva um programa para ler 6 números distintos, ou seja, não podem repetir. Exiba os números lidos.
"""
N = 6
i = 0
vetorA = [None]*N
 
def HAnoVetor(variavel, vetor):
    for i in range(N):
        if variavel == vetor[i]:
            return True
    return False                

while i < N:
    variavel = int(input("Digite um elemento para o vetor "))
    if not HAnoVetor(variavel,vetorA):
            vetorA[i] = variavel
           
    else:
        print("já tem!")
        continue
    
    i = i + 1     
               
print(f"{vetorA}")
    
    
            
            
