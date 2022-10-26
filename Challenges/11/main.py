# 11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
# segundo grau e mostre o valor de Delta.

a = float(input('Entre com o valor de A: '))
b = float(input('Entre com o valor de B: '))
c = float(input('Entre com o valor de C: '))
delta = b**2 - 4*a*c 
ordem = f'O valor de delta é {delta}'
print(ordem)