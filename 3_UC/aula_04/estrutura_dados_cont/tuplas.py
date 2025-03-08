"""
As tuplas são coleções ordenadas,porém são imutáveis.
Homogêneas e podem ser Heterogêneas
"""
# Declaração das tuplas
tamanhos = ("pequena","media","grande")
print(f'''
      🤳 Tamanhos disponiveis: {tamanhos}
      ''')

# Operações com tuplas

# Acessar itens
print("🍕Tamanho médio:",tamanhos[1]) 

# Verificar itens
print("✅ Existe tamanho grande?","grande" in tamanhos)