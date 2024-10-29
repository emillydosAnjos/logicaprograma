i = 0 
maior = 0
menor = 0
while ( i<25):
    i += 1
    idade = int(input('digite sua idade: '))
    altura = float(input('digite sua altura: '))
    peso = float(input('digite seu peso: '))
    if ( idade > 50 ):
        maior = maior +1
    else:
        menor = menor +1
print('a quantidade de pessoas maiores de 50 anos são ',maior)
print('a quantidade de pessoas com idade menor que 50 são ',menor)