# 16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
# fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
# já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
# quantos dias de vida um fumante perderá e exiba o total em dias.

nome_fumante = input('Qual é o nome do fumante? ')
cigarros_dia = float(input(' Quantos cigarros por dia você fuma? '))
fumante_anos = float(input(' Quantos anos você fuma? '))
menos_vida = cigarros_dia * 600
calculo = (menos_vida/60) * 60 / 24
ordem = f'O fumante {nome_fumante}, cigarros fumado por dia {cigarros_dia}, fuma ao total de {fumante_anos}. Perdeu no total de {calculo} dias de vida'
print(ordem)