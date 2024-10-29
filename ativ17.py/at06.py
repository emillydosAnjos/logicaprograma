mais = 0
menos = 10
bmenos = 0
bmais = 0
for i in range (3):
    num = int (input('digite o numero do aluno: '))
    altura = int(input('digite a altura do aluno em centimetros : '))
    if altura > mais:
        mais > altura
        bmais = num
    if altura < menos:      
        menos = altura 
        bmenos = num 
print('aluno mais alto', bmais)
print("aluno mais baixo", bmenos)