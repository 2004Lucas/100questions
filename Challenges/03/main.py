"""
3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no
final uma mensagem.
Ex:
Nome do Funcionário: Maria do Carmo
Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.
"""
# Declarando variavel para receber os dados:
nome_funcionario = str(input('Qual é o nome do funcionário? '))
salario_funcionario = float(input('Qual é o salário do funcionário? '))

print('O funcionário', nome_funcionario + ' tem um salário de ', salario_funcionario, ' em junho')