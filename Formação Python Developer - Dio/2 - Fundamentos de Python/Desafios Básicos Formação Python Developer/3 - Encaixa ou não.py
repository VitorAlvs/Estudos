N = int(input())

while(N > 0):
    A, B = input("Informe A e B, separado por um espaço: ").split()
    
    if A.endswith(B):
      print("encaixa")
    else:
      print("nao encaixa")
    
    N -= 1