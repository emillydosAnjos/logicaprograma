cod = int(input('qual o seu codigo? '))
venda = float(input('qual o seu total de vendas:'))
if (venda <= 100.00):
    print('num tem tlgd so fé po c ')
comi = 6/100*venda
if ( venda >100) and ( venda <=350):
    print('sua comissão é de {} '.format(comi))
comi2 = 10/100*venda
if (venda >350):
    print('sua comissao é de {}' .format(comi2))
    