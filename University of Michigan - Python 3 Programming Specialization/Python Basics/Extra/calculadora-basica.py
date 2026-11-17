def sub(num1,num2):
    if (num1 > num2):
        return num1-num2
    if (num2 > num1):
        return num2 - num1

def calc(arg, num1, num2):
    if (arg == "+"):
        return num1 + num2
    if (arg == "-"):
        if (sub(num1, num2) == None):
            return 0
        if (sub(num1, num2) != None):
            return sub(num1, num2)
    if (arg == "*"):
        return num1 * num2
    if (arg == "/"):
        return num1 / num2
    else:
        return "Digite uma operação válida"

arg = input("Digite a operação (+ - * /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


print(calc(arg, num1, num2))