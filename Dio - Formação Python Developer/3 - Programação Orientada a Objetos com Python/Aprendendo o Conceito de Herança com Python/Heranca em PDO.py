#Herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai

class A:
    pass

class B(A):
    pass

# Herança simples: A classe B herda de A
# Heraça múltipla: A classe C herda de A e B

class C:
    pass
class D(A, C):
    pass