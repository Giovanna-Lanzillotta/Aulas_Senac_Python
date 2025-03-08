# Carrinho de Compras 🛒​
# 💡 Enunciado:
# Crie um programa que permita adicionar produtos a um carrinho de compras.
#O programa deve continuar pedindo produtos até que o usuário digite "finalizar". No final, exiba todos os produtos comprados.
# 📝 Regras:
# O usuário digita o nome do produto e ele é adicionado a uma lista.
# Se o usuário digitar "finalizar", o programa encerra e mostra os produtos comprados.
# 🔍 Exemplo esperado:
# Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): Pizza
# Produto 'Pizza' adicionado ao carrinho!
# Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): Refrigerante
# Produto 'Refrigerante' adicionado ao carrinho!
# Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): finalizar

# 🛍️ Você comprou:
# - Pizza
# - Refrigerante

produtos = []
carrinho = []

while produtos != "finalizar":
    
    produtos = input("\n  Digite um produto no carrinho ou digite 'finalizar' para sair:")
    
    if produtos.lower() == "finalizar":
        #carrinho vazio
        if carrinho == []:
            print("❌ Nenhum produto foi comprado.")
            break
        else:
             print("Operação encerrada.")
        print(f"\n 🛍️ Você comprou: \n {carrinho}")
        break
       
    if carrinho.append(produtos):
        print(f" Produto '{produtos} foi adicionado ao carrinho!")
       
# if len(carrinho) > 0:
#     print(f" 🛍️ Você comprou:")
#     for item in carrinho:
#         print(f" 🔸 {item}")
# else:
#     print("❌ Nenhum produto foi comprado.") 