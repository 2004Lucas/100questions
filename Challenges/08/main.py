# 8) Desenvolva um programa que leia uma distância em metros e mostre os valores
# relativos em outras medidas.
# Ex:
# Digite uma distância em metros: 185.72
# A distância de 85.7m corresponde a:
# 0.18572Km
# 18.572Dam
# 1.8572Hm
# 1857.2dm
# 18572.0cm
# 185720.0mm

metro = float(input('Entre com algum valor: '))
ordem = f'A distância de {metro} corresponde a: quilômetro {metro / 1000}, decâmetro {metro / 10}, hectômetro {metro / 100}, decímetro {metro * 10}, centímetro {metro * 100}, milimetro {metro * 1000}'
print(ordem)