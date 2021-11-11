class ContaBancaria():
    def __init__(self, saldo, titular):
        self.saldo = float(saldo)
        self.titular = titular

    def __str__(self):
        return f'{self.titular} --> {self.saldo}'

#Child class
class Itau(ContaBancaria):
    def transferencia(self, valor, pessoa):
        total = (valor + (valor * 0.01))
        if total <= self.saldo:
            if self != pessoa:
                self.saldo -= total
                pessoa.saldo += valor
                print("Transação concluída!")
            else:
                print("Impossível transferir para sua própria conta")
        else:
            print('Saldo insuficiente!')

class Bradesco(ContaBancaria):
    def transferencia(self, valor, pessoa):
        total = (valor + (valor * 0.005 + 5))
        if total <= self.saldo:
            if self != pessoa:
                self.saldo -= total
                pessoa.saldo += valor
                print("Transação concluída!")
            else:
                print("Impossível transferir para sua própria conta")
        else:
            print('Saldo insuficiente!')


c1 = Itau(2800, "Matheus")
c2 = Bradesco(5000, "Isadora")

c1.transferencia(300,c2)
print(c1,"\n",c2)
