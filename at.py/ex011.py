impar = 0
par = 0
for i in range(10):
    valor = (int(input('informe o valor:')))
    if (valor%2 == 0):
        par = par + 1
    if (valor %2 == 1):
        impar = par - 1
print('numeros pares {}' .format(par))
print('numeros impares {}'.format(impar))