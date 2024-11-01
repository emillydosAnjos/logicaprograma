pedidos = []
quantidadepedidos = 0
soma = 0
while True:
    print('-'*20)
    print("Bem vindo a Pizzaria da mamãe Gecko\nQual será sua escolha de hoje? ")
    print('-'*20)
    pizza = str(input("Escolha o tamanho da pizza (pequena, média, grande:"))
    if pizza == "pequena":
       soma+=20
    if pizza == "media":
       soma +=30
    if pizza == "grande":
        soma += 40
    ingre = ['calabresa','mussarela','tomate','cebola','bacon']
    
    extra = input("Deseja adicionar um ingrediente extra temos (calabresa, mussarela, tomate, cebola, bacon)? (sim/não): ")
    if  extra == 'sim':
        ingrediente = int(input("Quantos ingredientes extras deseja adicionar? "))
        soma += ingrediente * 5
    refrigerante = input("Deseja beber um refrigerante? (sim/não):")
    if refrigerante == 'sim':
        soma += 8
    
    pedidos.append(soma)
    quantidadepedidos += 1
    print("Valor do pedido: R$",soma)

    continuar = input("Deseja fazer outro pedido? (sim/não): ")
    if continuar != 'sim':
        break

if pedidos:
    print(f"Pedido mais caro: R${max(pedidos)}")
    print(f"Pedido mais baixo: R${min(pedidos)}")
    print(f"Quantidade de pedidos realizados: {quantidadepedidos}")
else:
    print("Nenhum pedido foi realizado.")
