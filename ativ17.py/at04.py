
print('seguencia de fibonacci')
c = 16
t1 = 0 
t2 = 1
print(t1)
print(t2)
contador = 3
while contador <= c:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    contador +=1
print('fim')