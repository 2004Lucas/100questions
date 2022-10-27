# 21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
# BISSEXTO.

ano = int(input('Entre com um ano: '))
if ano % 4 == 0:
  print(f"O ano de {ano} é BISSEXTO!")
else:
  print(f"O ano de {ano} NÃO é BISSEXTO!")