# 18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar.

idade = int(input('Qual ano você nasceu? '))
calculo_idade = 2022 - idade
if calculo_idade >= 16:
    print('Parabéns, você pode votar!')
else:
    print('Que pena, você não pode votar no momento, mas daqui um tempinho ira poder. \n Por favor, aguarde!')
