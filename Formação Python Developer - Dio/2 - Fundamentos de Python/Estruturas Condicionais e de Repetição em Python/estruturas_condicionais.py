saldo = 500

def opcao():
    global saldo
    opcao = int(input("Se deseja realizar um saque, digite 1; se deseja realizar um depósito, digite 2 : "))
    if opcao == 1:
        valor = float(input("Digite um valor para retirar: "))
        sacar(valor)
    elif opcao == 2:
        valor = float(input("Digite um valor para depositar: "))
        depositar(valor)
    else:
        print("Opção inválida, tente novamente.")
    
def sacar(valor):
    global saldo
    if saldo >= valor:
        saldo -= valor
        print("Valor sacado!")
        print(f"Seu saldo atual é de R${saldo}.")
    else:
        print("Saldo insuficiente.1")
        opcao()

def depositar(valor):
    global saldo
    saldo += valor
    print(f"R${valor} foram adicionados a seu saldo.")
    print(f"Seu saldo atual é de R${saldo}.")

opcao()
