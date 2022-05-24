""" 
4. A tabela seguinte apresenta a quantidade de vendas dos fabricantes de veículos durante o período de 2013 a 2018, em múltiplos de mil unidades.

tabela na questão

Escreva um programa que:
• Armazene os dados da tabela em uma matriz;
• Determine e mostre o fabricante com maiores vendas em cada ano;
• Determine e mostre o ano onde houve o maior volume de vendas;
• Determine e mostre a média de vendas de cada fabricante no período apresentado na tabela.
5.

"""

# Armazene os dados da tabela em uma matriz;
from ntpath import join


matriz_A = [["Fabricante/Ano", "2013", "2014", "2015", "2016", "2017", "2018"],
            ["Chevrolet", 204, 323, 230, 257, 290, 222],
            ["Fiat     ", 295, 192, 198, 203, 308, 228],
            ["Foard    ", 220, 222, 317, 231, 245, 280],
            ["Volkswagen", 254, 262, 279, 284, 296, 230]]

matriz_B = [[ 204, 323, 230, 257, 290, 222], 
            [ 295, 192, 198, 203, 308, 228], 
            [220, 222, 317, 231, 245, 280], 
            [254, 262, 279, 284, 296, 230]]            

#Vizualizar matriz_A
print()
print("Matriz Completa com Nome das colunas e linhas! \n")
for i in range(5):
    for j in range(7):
        print(matriz_A[i][j] , sep=" ", end="\t")
    print()    

print()
print("Matriz completa apenas com os valores da matriz! \n")
#Vizualizar matriz_B    
for i in range(4):
    for j in range(6):
        print(matriz_B[i][j] , sep=" ", end="\t")
    print()    


# Determine e mostre o fabricante com maiores vendas em cada ano;
fabricante_ano = 0
lista_fabricante_vendas_ano = []
lista_fabricantes = ["Chevrolet", "Fiat", "Ford", "Volkswagen"]
ano = ["2013", "2014", "2015", "2016", "2017", "2018"]
fabricante = ""

def fabricante_maiores_vendas(matriz, i):
    
    maior = 0
    for j in range(4):
       maior =  matriz[j][i]
       for k in range(4):
           if maior < matriz[k][i]:
               maior = matriz[k][i]
               fabricante = lista_fabricantes[k]                                                      
    return fabricante      


for i in range(6):
    fabricante_ano = fabricante_maiores_vendas(matriz_B, i)
    lista_fabricante_vendas_ano.append(fabricante_ano)
    print(f'\n{ano[i]} - {lista_fabricante_vendas_ano[i]}')


# Determine e mostre o ano onde houve o maior volume de vendas



