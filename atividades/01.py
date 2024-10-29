#escreva um programa que receba 3 notas mostre a media aritmetica delas 
#e informe se o aluno foi aprovado ou reprovado a nota para ser aprovado deve ser maior que 7.
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
nota = (n1 + n2 + n3)/3
if (nota>=7):
    print(' O aluno foi aprovado')
else:
    print('o aluno foi reprovado')
    