"""
3. Escreva um programa que preencha uma matriz quadrada de ordem 3 com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente), calcule e exiba:
• A soma dos elementos de cada linha;
• A soma dos elementos de cada coluna;
• A soma dos elementos da diagonal principal da matriz;
• A soma dos elementos da diagonal secundária da matriz;
• A soma de todos os elementos da matriz.

"""

N = 3
matriz = [[None]*N for i in range(N)]

def soma_linhas(vetor):
    soma_linha = 0
    for i in range(N):
        soma_linha = soma_linha + vetor[i]
    return soma_linha        

def soma_colunas(vetor, i ):
    soma_coluna=0
    for j in range(N):
        soma_coluna = soma_coluna + vetor[j][i]
    return soma_coluna    

def soma_diagonal_P(vetor):
    soma_P = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                soma_P = soma_P + vetor[i][j]
    return soma_P            

def soma_diagonal_S(vetor):
    soma_D = 0
    for i in range(N):
        for j in range(N):
            if i + j == N - 1:
                soma_D = soma_D + vetor[i][j]
    return soma_D

def soma_elements(vetor):
    soma_All = 0   
    for i in range(N):
        for j in range(N):
            soma_All = soma_All + vetor[i][j]
    return soma_All         


linha = 0
for i in range(N):
    coluna = 0
    for j in range(N):
        matriz[i][j] = int(input(f'Digite o elemento da linha {linha+1} - coluna {coluna+1}:  '))
        coluna = coluna + 1 
    linha = linha + 1     

lista_linha = []
lista_coluna = []
for i in range(N):
    linha = soma_linhas(matriz[i])    
    coluna = soma_colunas(matriz, i)
    lista_linha.append(linha)
    lista_coluna.append(coluna)


diagonal_P = soma_diagonal_P(matriz)
diagonal_S = soma_diagonal_S(matriz)
soma_all = soma_elements(matriz)

print("\n") 
cont = 0
for i in lista_linha:
    print(f'A soma da {cont+1} linha é: {i} ')
    cont = cont + 1 
cont = 0   
for j in lista_coluna:
    print(f'A soma da {cont+1} coluna é: {j}')    
    cont = cont + 1 

print(f"A soma da diagonal principal é : {diagonal_P}")
print(f"A soma da diagonal secundaria é : {diagonal_S}")
print(f"A soma de todos os elementos da matriz é : {soma_all}")
