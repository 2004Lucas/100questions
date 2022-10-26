# 6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
# sucessor.
# Ex:
# Digite um número: 9
# O antecessor de 9 é 8
# O sucessor de 9 é 10

numero = int(input('Entre com um número inteiro: ( Exemplos de números inteiros: 1,2,3,4,5,6,7,8,9,10,11...)'))
ordem = f'O sucessor o antecessor do número apresentado {numero} é {numero - 1} e o {numero +1}'

print(ordem)