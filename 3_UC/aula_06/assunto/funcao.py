# SINTAXE BÁSICA DE UMA FUNÇÃO

def nome_da_funcao(parametros):
    #codigo da função
    resultado = 0
    return resultado

#função sem retorno
def ola_mundo():
   print(" 😁 Olá Mundo!")

ola_mundo() # Chamando a função (invocando a função)

#Função com parâmetros
def saudacao(nome):
    print(f" 😉 Olá seja bem vindo(a) {nome}")

saudacao("Giovanna")
saudacao("Willian")

# Função com parâmetros retorno
def somar(numero1,numero2):
    soma = numero1 + numero2
    return soma

print(somar(10,20))