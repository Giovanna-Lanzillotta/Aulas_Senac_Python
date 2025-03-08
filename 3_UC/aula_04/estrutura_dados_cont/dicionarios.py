"""
Os dicionários podem ser heterogêneos ou homogêneos
São ordenados, mutáveis e sempre são acompanhados por uma chave:valor
"""
# Declaração de um dicionário
cardapio = {
    "mussarela": 25.90,
    "calabresa":27.90,
    "frango com catupiry":29.90
}

print("📦 Cardápio da Pizzaria Sabores:",cardapio)

# Operações com dicionários

# 1. Acessar valores:
print("💰 Preço da pizza de calabresa: R$:",cardapio["calabresa"])

# 2. Adicionar itens:
cardapio["portuguesa"] = 30.90
print("⭐ Cardápio atualizado:",cardapio)

# 3.Alterar valores:
cardapio["mussarela"] = 26.90
print("🧀 Preço atualizado da mussarela:",cardapio["mussarela"])

# 4.Iterar sobre o dicionário:
for sabor,preco in cardapio.items():    #sabor e preco são variaveis temporarias  
    print(f'\n🍕A pizza de {sabor} custa R$ {preco:.2f}') 



