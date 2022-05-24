"""Uma matriz quadrada contendo valores inteiros é denominada quadrado mágico quando a soma dos 
elementos de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais 
principal e secundária são todos iguais. Por exemplo, a matriz seguinte é um quadrado mágico.
Escreva um programa que preencha uma matriz com valores fornecidos pelo usuário, determine e 
mostre se ela é um quadrado mágico.
"""

N = int(input("Digite a ordem da matriz: "))
matriz = [[None]*N for i in range(N)]

def soma_linhas(vetor):
    soma_linha = 0
    for j in range(N):
        soma_linha = soma_linha + vetor[j]
    return soma_linha   

def soma_colunas(vetor, i):
    soma_coluna = 0
    for j in range(N):
        soma_coluna = soma_coluna + vetor[j][i]    
    return soma_coluna    
        
def soma_diagonal_principal(vetor):
    soma_diagonal_P = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                soma_diagonal_P = soma_diagonal_P + vetor[i][j]
    return soma_diagonal_P

def soma_diagonal_secundari(vetor):
    soma_diagonal_secundari = 0
    for i in range(N):
        for j in range(N):
            if i + j == N - 1:
                soma_diagonal_secundari = soma_diagonal_secundari + vetor[i][j]
    return soma_diagonal_secundari            

linha = 0
for i in range(N):
    coluna = 0
    for j in range(N):
        matriz[i][j] = int(input(f'Digite o elemento da  {linha+1} linha - {coluna+1} coluna: '))
        coluna = coluna + 1       
    linha = linha + 1   

resultado = False
for i in range(N):
    linhas = soma_linhas(matriz[i])
    colunas = soma_colunas(matriz, i)
    diagonal_P = soma_diagonal_principal(matriz)
    diagonal_S = soma_diagonal_secundari(matriz)

    if linhas == colunas == diagonal_P == diagonal_S:
        resultado = True

if resultado == True:
    print(f'A matriz é um quadrado mágico!')
else:
    print(f'A matriz não é quadrado mágico!')    

