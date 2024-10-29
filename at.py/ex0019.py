rj = 0
bh = 0
sc = 0 
while True:
    num = input('digite sua cidade: ')
    if num == 'rj':
        rj =+1
    if num == 'bh':
        bh =+1
    if num == 'sc':
        sc =+1
    if num == 'fim':
        break
print('pessoas do rio de janeiro',rj)
print('pessoas de belo horizonte',bh)
print('pessoas de santa catarina',sc)