#escreva um programa ue leia o codigo de origem, de um produto e imprima 
# na tela a regiao de sua procedencia.
c = int(input('qual o codigo? '))
if(c ==1):
    print('sul')
if (c ==2):
    print('norte')
if (c ==3):
    print('lest')
if (c == 4):
    print('oeste')
if (c == 5) or (6 == c):
    print('nordeste')
if (c == 7) or (8 == c) or (9 == c):
    print('sudeste')
if (c == 10):
    print('centro-oeste')
if (c == 11):
    print('noroeste')
if (c >11):
    print('nao é um codigo')