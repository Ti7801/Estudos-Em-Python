"""
3. Escreva um programa para ler 6 números. Após a leitura dos números, verifique, 
para cada um deles, se é distinto, ou seja, não possui repetição.
"""

# O PROGRAMA TEM QUE VERIFICAR SE TODOS OS ELEMENTOS SÃO DISTINTOS. O USUÁRIO DIGITA DE QUALQUER FORMA.

N = 6
vetorNumeros = [None]*6
repetidos = [0]*N

for i in range(N):
    vetorNumeros[i] = int(input("Digite um elemento para o vetor:"))
    
for i in range(N):
    aux = vetorNumeros[i]
    for j in range(N):
        if aux == vetorNumeros[j]:
          repetidos[i] = repetidos[i] + 1 
          
#mostrar os números que se repetem e suas posições    
for i in range(N):
    if repetidos[i]>1:
        print(f'Posição[{i}] = {vetorNumeros[i]}')
    
    
# se todas as posições do vetor repetidos forem igual a 1 retorn True
        
def naoHarepetidos():
    for i in range(N):
        if repetidos[i] != 1:
            return True
    return False

if not naoHarepetidos():
    print(f'Não há repetidos!')    
    

        
            
            
            
            
            
    
        