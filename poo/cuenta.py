class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.__saldo= saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("cantidad inválida.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("cantidad  inválida.")

    def imprimirsaldo(self):
        print("El saldo de la cuenta es:", self.__saldo)

cuenta1= Cuenta(1111,3000)
print(cuenta1.numero)  
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.imprimirsaldo()
