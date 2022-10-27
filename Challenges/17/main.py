# 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
# o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade_carro = float(input('Qual é a velocidade do carro? '))
if velocidade_carro > 80:
    print('Parabéns, você conseguiu ser multado por passar a velocidade! :)   seja feliz com a conta pra pagar')
    multa = (velocidade_carro - 80) * 5
    print(f'O valor da sua multa é {multa}, caso não pague tera juros :) ')