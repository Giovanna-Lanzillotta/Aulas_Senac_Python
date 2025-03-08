"""
Homogêneo -> Aceita apeanas um  tipo de dado
Heterogêneo -> Aceia dados de tipos diferentes
As estruturas de dados são delaradas com snake_case
"""
# Declaração listas []
# Ordenadas,mutáveis e hetetogêneas

sabores = ["mussarela","calabresa","frango com catupiry","portuguesa"]
dados_pizza = ["mussarela", 26.90 , True]
# print("Sabores disponiveis: ",sabores)
# print("Informações da pizza: ",dados_pizza)

#Operações com listas 

#1. append() -> Adicionar um novo valor ao final da lista.
sabores.append("margherita") 
sabores.append("pepperoni") # É necessário adicionar um de cada vez
print("Sabores disponiveis: ",sabores)

#2. remove() ->Remove um elemento da lista
sabores.remove("calabresa")
print("Sabores disponiveis: ",sabores)

#3. Acessando os elemento. []
pizzas = ["mussarela","calabresa","frango com catupiry","portuguesa"]
print(pizzas[0])
print(pizzas[-1]) #Acessa o último indice da lista