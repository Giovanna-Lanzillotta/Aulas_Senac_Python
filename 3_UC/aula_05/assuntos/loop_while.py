sabores = ["Mussarela","Calabresa","Pepperroni","Quatro queijos","Frango com catupiry"]
pedido = ""

print("🍕 Faça seu pedido(digite 'sair' para encerrar): ")
while pedido.lower() != 'sair':
    pedido = input("Escolha um sabor de pizza do cardápio: ")
    if pedido in sabores:
        print(f'🙆‍♀️ {pedido} adicionado ao seu pedido!')
    elif pedido.lower() == "sair":
        print("📉 Pedido encerrado!")
    else:
        print("❌ Esse sabor no está não cardápio. Escolha outro sabor.")
    