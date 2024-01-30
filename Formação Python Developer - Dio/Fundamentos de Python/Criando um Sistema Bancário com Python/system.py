extrato_lista = []
quant_saque = 0
quant_max_saque = 3
valor_max_saque = 500
saldo = 0


while quant_saque < quant_max_saque:
    def menu():
        global saldo
        opcao = input("Se deseja realizar um saque, digite 1; se deseja realizar um depósito, digite 2; se deseja vizualizar o extrato, digite 3: ")
        if int(opcao) == 1:
            valor = float(input("Digite um valor para retirar: "))
            sacar(valor)
        elif int(opcao) == 2:
            valor = float(input("Digite um valor para depositar: "))
            depositar(valor)
        elif int(opcao) == 3:
            mostrar_extrato()
        else:
            print("Opção inválida, tente novamente.")
            menu()
        
    def sacar(valor):
        global saldo
        global quant_saque
        global quant_max_saque
        global valor_max_saque
        if valor > 0:
            if quant_saque <= quant_max_saque:
                if valor <= valor_max_saque:
                    if saldo >= valor:
                        saldo -= valor
                        print("Valor sacado!")
                        print(f"Seu saldo atual é de R$ %.2f." %saldo)
                        extrato_lista.append(f"Saque          	  R$ %.2f." %saldo)
                        quant_saque += 1
                    else:
                        print("Saldo insuficiente.")
                        menu()
                else:
                    print(f"O valor máximo para saques é de R$R$ %.2f, por isso não foi possíver realizar o saque" %valor_max_saque)
                    menu()
            else: 
                print("Quantidade máxima de saques diários atingida. ")
                menu()
        else: 
            print("Não é possível sacar valores nulos ou negativos.")
            menu()

    def depositar(valor):
        global saldo
        if valor > 0:
            saldo += valor
            print(f"R${round(valor, 2)} foram adicionados a seu saldo.")
            print(f"Seu saldo atual é de R$ %.2f." %saldo)
            extrato_lista.append(f"Deposito          R$ %.2f." %saldo)
        else:
           print("Não é possível sacar valores nulos ou negativos.")
           menu()

    def mostrar_extrato():
        print("\n*******************EXTRATO*******************")
        if extrato_lista == []:
            print("Não houveram movimentações")
        else:
            for each in extrato_lista:
                print(each, "\n")
        print("*********************************************")

    menu()
