"""
O Brasil possui 26 estados e 1 distrito federal, totalizando 27 unidades federativas. 
Escreva um programa para armazene, em um vetor, a sigla de todas as unidades federativas.
O programa deverá obter de vários usuários qual é a unidade federativa ele acha mais interessante,
informando a respectiva sigla. O programa encerra quando for digitada uma sigla inexistente. 
Ao final, o programa deverá exibir qual foi a sigla mais votada (considere possibilidade de empate).
"""

todas_unidades = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA","MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO",]
N_votos = int(input("Digite a quantidade de Unidades Federativas você deseja: "))
M_uf = 27
votos = [None] * N_votos
contadores = [0] * M_uf
maior_valor = 0
lista = []

#Função que válida se a sigla existe no vetor todas_unidades
def isValidVote(v_maiuscula):
    for j in range(M_uf):
        if v_maiuscula == todas_unidades[j]:
            return True
    return False

def most_voted(vetor_votos, all_unidades):
    #Preenchendo o vetor contadores com a repetição de cada sigla.
    for i in range(M_uf):
        uf = all_unidades[i]
        for j in range(N_votos):
            if uf == vetor_votos[j]:
                contadores[i] = contadores[i] + 1     
    #Encontrando no vetor contadores a posição do maior valor do vetor.                    
    aux = contadores[0]
    posicao = 0
    sigla = ""
    for i in range(M_uf): 
        if aux < contadores[i]:
            aux = contadores[i]
            posicao =  i
    
    for i in range(M_uf):
        if contadores[posicao] == contadores[i]:
            lista.append(i)
            
    sigla = [None] * len(lista)
    uf = 0
    
    for i in range(len(lista)):
        uf = lista[i]
        sigla[i] = all_unidades[uf]
                          
    return sigla       
                            
for i in range(N_votos):
    variavel = input("Digite uma unidade federativa: ")
    variavel_maiuscula = variavel.upper()
  
    if isValidVote(variavel_maiuscula):
        votos[i] = variavel_maiuscula
    else:
        print("Sigla inexistente!")    
        break
#Atribuindo a sigla mais voltada a variavel mais_votadas!    
mais_votadas = most_voted(votos, todas_unidades)    
    
print(f"A sigla mais voltada foi: {mais_votadas}")

