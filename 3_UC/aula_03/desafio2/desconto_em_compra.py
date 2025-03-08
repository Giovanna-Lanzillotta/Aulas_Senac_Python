# A conta da Mariana, cliente da pizzaria Sabores, `ficou no valor de R$ 120` e ela quer saber se tem direito a desconto.
# Tendo como base o valor do pedido, `escreva um programa que verifique se ela tem direito ao desconto.`

# Use:
# `10% para pedidos acima de R$ 50.`
# `20% para pedidos acima de R$ 100.`

valor_pedido = float(input("Qual foi o valor do pedido?"))

if valor_pedido > 50 and valor_pedido <= 100:
    desconto = valor_pedido * 0.10
    preco_final = valor_pedido - desconto
    print(f"O valor {valor_pedido} teve um desconto de 10% com o valor final de {preco_final}")
elif valor_pedido > 100:
     desconto = valor_pedido * 0.20
     preco_final = valor_pedido - desconto
     print(f"O valor {valor_pedido} teve um desconto de 20% com o valor final de {preco_final}")