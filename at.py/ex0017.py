i = 0
maior = 0
maior2 = 0
maior3 = 0
maior4 = 0
menor = 0
while True:
    num = int(input('digite um numero: '))
    if (num < 0 ):
        break
    if  ( num >0 ) and (num <=25):
        maior += 1
    if  ( num >26 ) and (num <=50):
        maior2 += 1
    if  ( num >51 ) and (num <=75):
        maior3 += 1   
    if  ( num >76 ) and (num <=100):
        maior4 += 1  
   
        
print('dentro do intervalo [0,25]: ',maior)
print('dentro do intervalo [26,50]: ',maior2)
print('dentro do intervalo [51,75]: ', maior3)
print('dentro do intervalo [76,100]: ',maior4)
   
       