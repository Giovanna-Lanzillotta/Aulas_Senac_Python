"""
Os conjuntos não são ordenados,são mutáveis,heterogêneos e homogêneos e não permitem elementos duplicados.
"""
# Declaração dos conjuntos
ingredientes = {"mussarela","calabresa","tomate","azeitona","tomate"}
print("🍳 Ingredientes básicos:",ingredientes)

# Operações com conjuntos

# Adicionar items:
ingredientes.add("oregáno")
print("⭐ Ingredientes atualizados:",ingredientes)

# Remover items:
ingredientes.remove("tomate")
print("❌ Ingredientes após a remoção:",ingredientes) #os dois tomates foram removidos

# União de conjuntos:
adicionais = {"bacon","palmito"}
todos_ingredientes = ingredientes.union(adicionais)
print("🍅 Todos os ingredientes:",todos_ingredientes)

# Interseção de conjuntos: Aparecem em ambos os conjuntos
pizza_vegana = {"tomate","azeitona","rúcula"}
comuns = ingredientes.intersection(pizza_vegana)
print("🥦 Ingredientes comuns:",comuns)