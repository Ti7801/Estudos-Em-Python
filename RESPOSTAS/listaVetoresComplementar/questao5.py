"""
Faça um programa para ler as 8 dezenas apostadas por 20 apostadores 
e verificar se a aposta é válida (cada dezena está entre [1, 80] e não pode haver repetição). O programa 
deverá calcular e exibir a quantidade de números acertados em cada aposta.
Atenção! As dezenas sorteadas são: 06, 07, 13, 14 e 26.
"""
# cada jogador aposta 8 dezenas, são 20 jogadores!

ncol=3
nlinh = 3
i=0
j=0
valor = 0
m = [[None]*ncol for i in range(nlinh)]
vetor = [None]* ncol
vetor_correto = [6, 7, 13, 14, 26]
Qtd_vetor_correto = 5
apostas = 0
vetor_aposta = [None]*nlinh


def ExisteNoVetor(variavel, vetor):
    for i in range(ncol):
        if variavel == vetor[i]:
            return True
    return False


def resultado_apostas(vetor_preenchido):
    for i in range(nlinh):
        apostas = 0
        for j in range(ncol):
            valor = vetor_preenchido[i][j] 
            for w in range(Qtd_vetor_correto):
                if valor == vetor_correto[w]:
                    apostas = apostas + 1            
        vetor_aposta[i] = apostas
    
    return vetor_aposta  

while i < nlinh:    
    print(f"Digite as {ncol} dezenas do {i+1} jogador!")
    j = 0
    while j < ncol:    
        variavel = int(input("Digite uma dezena: "))
        if variavel > 0 and variavel <= 80:
            if not ExisteNoVetor(variavel, m[i]):
                m[i][j] = variavel
            else:
                print("Este número ja existe, digite outro!")
                continue
        else:
            print("As dezenas digitadas devem ser entre 01 e 80!")
            print("Digite um novo valor!")
            continue   
        j = j + 1
    i = i + 1         

resultado = resultado_apostas(m)
print(f"O número de acertos em cada aposta foi : {resultado}")  
          
         

