import random

num = random.randint(1, 100)

def adivinhar():
    numero_adv = int(input("Adivinhe o número gerado: "))

adivinhar()

if numero_adv > num:
        print(f"{numero_adv} é maior que o número gerado")
        adivinhar()
elif numero_adv < num:
        print(f"{numero_adv} é menor que o número gerado")
        adivinhar()
elif numero_adv == num:
        print(f"Voê acertou, o número gerado foi {num}")
        adivinhar()

