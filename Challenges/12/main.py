# 12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
# PREÇO PROMOCIONAL, com 5% de desconto.


nome_produto = input('Digite o nome do produto: ')
produto = float(input(f'Digite o preço do {nome_produto}: '))
desconto = produto * 5/100
ordem = f'O {nome_produto} com 5% de desconto ira custar: {produto - desconto} '
print(ordem)