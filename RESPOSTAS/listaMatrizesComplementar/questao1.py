"""
Uma matriz de permutação é uma matriz quadrada cujos elementos são 0's ou 1's,
tal que em cada linha e em cada coluna exista apenas um elemento igual a 1. Por exemplo, a matriz seguinte é uma matriz de permutação.

"""
# Construir uma função que verifica linha que o número estar.
# Construir uma função que verifica coluna que o número estar.

from math import fabs


N = int(input('Digite a ordem da matriz: '))

matriz = [[None]*N for i in range(N)]

def verifica_se_so_tem_1_linha(vetor):
    cont = 0
    for i in vetor:
        if i == 1:
            cont =  cont + 1
    if cont == 1:
        return True
    else:
        return False             
 
def verifica_se_so_tem_1_coluna(vetor):
    cont = 0
    for i in vetor:
        if i == 1:
            cont = cont + 1 
    if cont == 1:
        return True
    else:
        return False            

def pegar_coluna(vetor, ordem, i):
    lista_colunas = []
    for j in range(ordem):
        lista_colunas.append(vetor[j][i])
    return lista_colunas    

linha=1
for i in range(N):
    coluna=1
    for j in range(N):
        matriz[i][j] = int(input(f'Digite o elemento da linha {linha} - coluna {coluna}: '))
        coluna = coluna + 1
    linha = linha + 1    
 
ehPermutacao = True

for i in range(N):
    if not verifica_se_so_tem_1_linha(matriz[i]): # verificando todas as linhas
        ehPermutacao = False

for i in range(N):
    coluna_da_vez = pegar_coluna(matriz, N, i)
    if not verifica_se_so_tem_1_coluna(coluna_da_vez):  #verificando todas as colunas
        ehPermutacao = False

if (ehPermutacao):
    print("É uma matriz de permutacao!")
else:
    print("Não é uma matriz de permutação!")    

