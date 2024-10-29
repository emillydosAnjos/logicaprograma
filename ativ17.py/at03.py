
nome = str (input('qual seu nome? '))
len = len (nome)
if len >=3: 
 idade = int(input('digite sua idade: '))
if idade >0 and idade < 150 :
 salario = int (input('qual o seu salario? '))
if salario > 0 :
 sexo = str (input('qual o seu sexo f ou m?'))
if sexo == 'f' or 'm':
 estado = str(input('digite seu estado civil ? s, c, v, d, : '))
if estado == 's' or 'c' or 'v' or 'd':
    print('valido')
else: 
    print('invalido')