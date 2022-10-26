# 7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
# sua terça parte.
# Ex:
# Digite um número: 3.5
# O dobro de 3.5 é 7.0
# A terça parte de 3.5 é 1.16666

numero = float(input('Entre com um número: '))
ordem = f'O dobro de {numero} é {numero * 2}, e a terça parte é {numero / 3}'
print(ordem)