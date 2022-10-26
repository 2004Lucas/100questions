# 9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

dinheiro = float(input('Quanto de dinheiro você tem? '))
ordem = f'O total de dollares que você pode adquirir é {dinheiro / 5.35}'
# valor do dollar no dia 26/10/2022 as 14:20, de real pra dollar
print(ordem)