#1
class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular   = titular.upper()
        self._saldo     = saldo
        self._estado    = False

#2
class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular   = titular.upper()
        self._saldo     = saldo
        self._estado    = False
    
    def __str__(self):
        return f'{self._titular} | {self._saldo}'
    
contaPedro = ContaBancaria('pedro da silva', 345)
contaMarco = ContaBancaria('marco deAngelo', 2933)
print(contaPedro)
print(contaMarco)

#3
class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular   = titular.upper()
        self._saldo     = saldo
        self._estado    = False
    
    def __str__(self):
        return f'{self._titular} | {self._saldo} | {self._estado}'
    
    @property
    def alternar_estado(self):
        self._estado = not self._estado

contaPedro = ContaBancaria('pedro da silva', 345)
contaPedro.alternar_estado()
print(contaPedro)