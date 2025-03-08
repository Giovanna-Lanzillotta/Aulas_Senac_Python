# 3. **Atualizar Cardápio**
    
# `Crie` um `dicionário para o cardápio` e 
# `adicione um novo sabor com preço`. 
# `Atualize` o preço de um sabor existente e 
# `remova` um sabor do cardápio.

cardapio = {
    "mussarela" : 21.90,
    "margherita" : 24.90,
    "presunto" : 25.90,
    "calabresa" : 26.90,
    "portuguesa" : 27.90
}
print("cardapio:",cardapio)

cardapio["frango com catupiry"] = 29.90
print("Cardapio atualizado:",cardapio)

cardapio["portuguesa"] = 28.90
print("Cardapio após alteração de preço:",cardapio)

del cardapio["margherita"]
print("Cardapio depois de remover sabor: ",cardapio)