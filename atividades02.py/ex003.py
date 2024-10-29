for i in range(1,101):
    n = int(input('digite um numero: '))
if n > 0 :
    soma = n * i
    media = soma / i
    print('a soma é de {} e a media é de {}' .format(soma, media))
else:
    print('erro irmao')