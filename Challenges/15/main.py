# 15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
# salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
# por hora trabalhada.

dias_trabalho = float(input('Entre com os dias trabalhados: '))
horas_contribuidas = float(input('Entre com a hora que tu trabalha por dia: '))
contribuicao = horas_contribuidas * 25

ordem = f'Pelos seus dias contribuidos {dias_trabalho}, e com suas horas de contribuição {horas_contribuidas}, o seu dia de trabalho custa {contribuicao}, e todos os seus dias de trabalho custam {dias_trabalho * (contribuicao)} '
print(ordem)