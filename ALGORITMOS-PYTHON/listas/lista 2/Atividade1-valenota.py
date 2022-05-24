"""
Exercício Valendo nota - Python- TSI - 100 pontos
"""

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
nota4 = float(input('Digite a quarta nota do aluno: '))

soma = 0

if nota1 <= nota2 and nota1 <= nota3 and nota1 <= nota4:
    soma = nota2 + nota3 + nota4
elif nota2 <= nota1 and nota2 <= nota3 and nota2 <= nota4:
    soma = nota1 + nota3 + nota4
elif nota3 <= nota1 and nota3 <= nota2 and nota3 <= nota4:
    soma = nota1 + nota2 + nota4
elif nota4 <= nota1 and nota4 <= nota2 and nota4 <= nota3:
    soma = nota1 + nota2 + nota3

media = float(soma / 3)

if media >= 9.0:
    print(f'O aluno obteve a média : {media} e o conceito A. Logo está Aprovado!!!')
elif media >= 8.0 and  media < 9.0:
    print(f'O aluno obteve a média : {media} e o conceito B. Logo está Aprovado!!!')
elif media >= 6.0 and media < 8.0:
    print(f'O aluno obteve a média : {media} e o conceito C. Logo está Aprovado!!!')
elif media >= 4.0 and media < 6.0:
    print(f'O aluno obteve a média : {media} e o conceito D. Logo está Reprovado!!!')
elif media < 4.0:
    print(f'O aluno obteve a média : {media} e o conceito E. Logo está Reprovado!!!')













