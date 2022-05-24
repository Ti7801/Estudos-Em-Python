"""
Exercício 2 Valendo nota - Python- TSI - 100 pontos
"""

# Valores lidos para o desenvolvimento da questão
nome = input('Digite o nome do hóspede: ')
tipo_apartamento = input('Digite o tipo de apartamento - A,B,C ou D: ')
numero_diarias = int(input('Digite o número de diárias utilizadas pelo hóspede: '))
valor_consumo_interno = float(input('Digite o valor do consumo interno do hóspede: '))

valor_diaria = 0
valor_total_diaria = 0
subtotal = 0
total_geral = 0
valor_unitario_diaria = 0
valor_taxa_servico = 0
# Condições para a escolha do tipo de apartamento.
if tipo_apartamento == 'A':
    valor_total_diaria = numero_diarias * 150.00
    valor_unitario_diaria = 150.00
elif tipo_apartamento == 'B':
    valor_total_diaria = numero_diarias * 100.00
    valor_unitario_diaria = 100.00
elif tipo_apartamento == 'C':
    valor_total_diaria = numero_diarias * 75.00
    valor_unitario_diaria = 75.00
elif tipo_apartamento == 'D':
    valor_total_diaria = numero_diarias * 50.00
    valor_unitario_diaria = 50.00

# Calculos para resolução
subtotal = valor_total_diaria + valor_consumo_interno
valor_taxa_servico = subtotal * 0.10
total_geral = subtotal + valor_taxa_servico

print(f'Nome do Hospede: {nome}')
print(f'Tipo do Apartamento: {tipo_apartamento}')
print(f'Número de Diárias: {numero_diarias}')
print(f'Valor Unitário da Diária: {valor_unitario_diaria}')
print(f'Valor Total das Diárias: {valor_total_diaria}')
print(f'Valor do Consumo Interno: {valor_consumo_interno}')
print(f'O Subtotal: {subtotal}')
print(f'Valor da Taxa de Serviço: {valor_taxa_servico}')
print(f'Total Geral: {total_geral}')



