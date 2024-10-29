contador = 0
fora = 0
for i  in range(0,5):
    v = int(input('digite um numero: '))
    if ( v>=10) and ( v <=20):
        contador = contador +1
    else:
        fora = fora + 1
print('numero do intevalo é [10, 20]',contador)
print('numero fora do intervalo',fora)   
