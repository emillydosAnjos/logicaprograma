i = 0
jose = 0
joao = 0 
maria = 0
meunego = 0
nulo = 0
branco = 0
while (i < 6):
    candidato =  int(input('digite o codigo do candidato: '))
    if (candidato == 1):
        jose += 1
    if (candidato == 2):
       joao += 1
    if (candidato == 3):
       maria += 1
    if (candidato == 4):
       meunego += 1
    if (candidato == 5):
       nulo +=1
    if (candidato == 6):
        branco+= 1
    if(candidato >= 7):
        print('invalido')
        i = 7
soma = nulo/(jose + joao+ maria+ meunego) *100
soma2 = branco/(jose+ joao+ maria+ meunego) *100
print (' o total de votos para josé são de : ',jose)
print (' o total de votos para joao são de : ',joao)
print (' o total de votos para maria são de : ',maria)
print (' o total de votos para meu nego são de : ',meunego)
print (' o total de votos nulos são de : ',nulo)
print (' o total de votos brancos são de : ',branco)
print('votos em nulo',soma)
print('votos em branco',soma2)
