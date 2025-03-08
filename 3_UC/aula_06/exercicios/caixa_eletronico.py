# Caixa Eletrônico 💰​
# 💡 Enunciado:
# Crie um programa que simule um caixa eletrônico. O usuário deve poder sacar valores até que o saldo disponível acabe ou até que ele digite "sair".
# 📝 Regras:
# Comece com um saldo inicial de R$ 500.
# Peça para o usuário digitar um valor para saque.
# Se o valor for maior que o saldo, avise que não há saldo suficiente.
# Se o usuário digitar "sair", encerre o programa.
# 🔍 Exemplo esperado:
# Saldo disponível: R$ 500
# Digite o valor para sacar ou 'sair' para encerrar: 200
# Saque realizado! Novo saldo: R$ 300
# Digite o valor para sacar ou 'sair' para encerrar: 400
# ❌ Saldo insuficiente!
# Digite o valor para sacar ou 'sair' para encerrar: sair
# 🏦 Operação encerrada.

saldo = 500  # Valor referente ao saldo inicial do usuário

while saldo > 0: # O laço while continuará sendo executado até que o saldo acabe(False).
    print(f' \n💰 Saldo disponível: R$ {saldo:.2f}') # \n realiza uma quebra de linha.
    saque =input("💲 Digite o valor para sacar ou 'sair' para encerrar: ") # a variavel saque nasceu no while

    # o if está dentro do while
    if saque.lower() == "sair": # O método lower() transforma string em minúscula.
        print("🏦 Operação encerrada. ")
        break # Comando que realiza a quebra do loop mais próximo.

    saque = float(saque) # float() método que converte explicitamente o valor para float(valor decimal).
    if saque > saldo:
        print("❌ Saldo insuficiente!")
    else:
        # saldo = saldo - saque # Redeclaração da variável saldo.
        saldo -= saque # Operação de decremento (subtração e reatribuição ao mesmo tempo.)
        print(f" 💸 Saque de R$ {saque:.2f} realizado!")