# 14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
# um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
# sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

quantidade_km = float(input('Quantos km foi percorrido? '))
quantidade_dias = float(input('Quantos dias o carro foi alugado? '))

calculo_dias = quantidade_dias * 90
calculo_km = quantidade_km * 0.20

ordem = f'O carro andou a quantidade de {quantidade_km}km, e foi alugado por {quantidade_dias}, no total de dias o valor foi {calculo_dias}, e o de km foi de {calculo_km}'
print(ordem)