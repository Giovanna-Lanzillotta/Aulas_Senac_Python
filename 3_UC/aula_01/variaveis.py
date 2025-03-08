"""Pizzaria Sabores
Calabresa, Mussarela, Frango
grande"""


# pizza = "Calabresa" # Declarando a variável e inicializando  #HardCode
pizza = input("Informe o sabor da pizza:")

TAMANHO_DA_PIZZA = "grande" # Constante Fake :D
preco = 29.90
print(f"""
==========================================
     A pizza escolhida é de {pizza}
     a pizza é {TAMANHO_DA_PIZZA}
     e o valor é de {preco}
==========================================
 """)
