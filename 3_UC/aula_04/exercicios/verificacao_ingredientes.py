# 2. **Verificação de Ingredientes**
    
# Dado dois conjuntos de ingredientes, `exiba os ingredientes comuns entre eles` e 
# os `que estão disponíveis apenas em um conjunto.`

ingredientes_principais = {"queijo","molho","tomate","oregáno"}
ingredientes_adicionais ={"calabresa","azeitona","palmito","tomate"}

comuns = ingredientes_principais.intersection(ingredientes_adicionais)
print("Ingredientes comuns:",comuns)

disponiveis = ingredientes_principais.symmetric_difference(ingredientes_adicionais)
print("Ingredientes disponíveis:",disponiveis)