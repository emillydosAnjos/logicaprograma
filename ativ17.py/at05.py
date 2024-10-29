pri = int (input('digite um numero e descubra se é um numero primo :'))
if pri > 1:
    for i in range (2 , pri):
     if (pri % i == 0 ):
        print('é não numero primo')
        break
    else:
        print( 'é um numero primo')
        
else:
    print('não é um numero primo')