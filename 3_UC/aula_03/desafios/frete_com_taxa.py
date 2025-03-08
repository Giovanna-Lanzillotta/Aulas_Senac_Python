# Agora, a nossa pizzaria está cobrando uma `taxa fixa de R$5 por entrega`, além de `R$1 por km até 5km,` e `R$2 por km até 10km`. 
# Mais ainda `não entregamos com a distância superior a 10km`.

# Pegando como base essas possibilidades, faça um programa que responda as seguintes perguntas:

# - Quanto Joana irá pagar de frete, sendo que mora a 8km da pizzaria.
# - Quanto Guilherme irá pagar de frete, sendo que mora a 3km da pizzaria.
# - Quanto Rafael irá pagar de frete, sendo que mora a 11km da pizzaria.

distancia = float(input("Qual a sua distância? "))

if distancia <= 5:
    taxa = distancia * 1
    taxa_total = taxa + 5
    print("💰 A sua taxa é de R$ ",taxa_total)
elif distancia <= 10:
    taxa = distancia * 2
    taxa_total = taxa + 5
    print("💰 A sua taxa é de R$ ",taxa_total) 
else :
    print("❌Não entregamos com distância superior a 10 km")