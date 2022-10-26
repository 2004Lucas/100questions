# 5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
# Ex:
# Nota 1: 4.5
# Nota 2: 8.5
# A média entre 4.5 e 8.5 é igual a 6.5

nome_aluno = str(input('Qual é o nome do aluno? '))
nome_materia = str(input('Qual é o nome da matéria? '))

nota1 = float(input(f"Qual foi a primeira nota do aluno {nome_aluno} na materia de {nome_materia}? "))
nota2 = float(input(f"Qual foi a segunda nota do aluno {nome_aluno} na materia de {nome_materia}? "))

media = (nota1 + nota2) / 2
print(f'As notas do aluno(a) {nome_aluno} são {nota1} {nota2} com isso a média final é: {media} ')

if media >= 10 :
    print(f'parabens {nome_aluno}, você passou no teste')
else:
    print(f'Que pena meu(minha) caro(a) aluno(a) {nome_aluno}, você reprovou no teste, mas fique calmo que ainda tem a recuração! :)')


