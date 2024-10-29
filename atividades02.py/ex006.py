contador = 0
fora = 0
for i in range (1,51):
    n = int(input('digite um numero: '))
    if ( n <= 0):
        contador = contador +1
    else:
        fora = fora + 1
print('existem {} numeros negativos'.format(contador))