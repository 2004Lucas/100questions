# 19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
# não um bom aproveitamento (se ficou acima da média 7.0).

aluno = input('Qual é o nome do aluno? ')
nota1 = float(input(f'Qual foi a primeira nota do(a) {aluno}? '))
nota2 = float(input(f'Qual foi a segunda nota do(a) {aluno}? '))

calculo_media = (nota1 + nota2) / 2

if calculo_media >= 7:
    print(' Teve aproveitamento!')
else:
    print('Não teve muito aproveitamento!')