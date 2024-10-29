mP = 0
mM = 0
mG = 0
mGG = 0
for i in range(0,500):
    tamanho = input("Informe o tamanho da camiseta: ")
    if tamanho == "P":
       mP += 1
    elif tamanho == "M":
        mM += 1
    elif tamanho == "G":
        mG += 1
    elif tamanho == "GG":
       mGG += 1
    else:
        print("Tamanho inválido. Informe P, M, G ou GG.")
print("Total de camisetas:")
print("Tamanho P:", mP)
print("Tamanho M:", mM)
print("Tamanho G:", mG)
print("Tamanho GG:",mGG)