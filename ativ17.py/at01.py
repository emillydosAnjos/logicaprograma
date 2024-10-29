#calcular o peso ideal 
pessoa = str (input('digite seu sexo: '))
altura = float(input('digite sua altura: '))
if ( pessoa == 'homem'):
    pesoh = (72.7*altura) -58
    print('sua altura ideal é de {}'.format(pesoh))
if (pessoa == 'mulher'):
    pesom = (62.1*altura) -44.7
    print('sua altura ideal é de {}'.format(pesom))