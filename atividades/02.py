#escreva um programa que receba um numero inteiro de 1 a 12 
# e imprima na tela o seu mes correspodente. se o numero não
# estiver no intervalo [1, 12] informe que o mes solicitado é invalido.
m = int(input(' digite um numero: '))
if (m ==1):
   print('seu mes é janeiro')
if (m == 2):
   print('seu mes é fevereiro')
if (m == 3):
   print('seu mes é março ')
if (m ==4):
   print('seu mes é abril')
if (m == 5):
   print('seu mes é maio')
if (m == 6):
   print('seu mes é junho ')
if (m ==7):
   print('seu mes é julho')
if (m ==8):
   print('seu mes é agosto')
if (m == 9):
   print('seu mes é setembro')
if (m == 10):
   print('seu mes é outubro ')
if (m ==11):
   print('seu mes é novembro')
if (m == 12):
   print('seu mes é desembro')
if (m >12):
   print('{} não é um mes' .format(m))