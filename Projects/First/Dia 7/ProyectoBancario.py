class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numcuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numcuenta=numcuenta
        self.balance=balance
    def depositar(self,cantidad):
        self.balance+=cantidad
    def retirar(self,cantidad):
        self.balance-=cantidad
class Persona2:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente2(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")


def crear_cliente():
    nombrec=input("Ingrese el Nombre del Cliente: ")
    apellidoc = input("Ingrese el Apellido del Cliente: ")
    numecuentac = input("Ingrese el Numero de Cuenta del Cliente: ")

    mi_cliente=Cliente(nombrec, apellidoc, numecuentac)
    return mi_cliente
def inicio():
    cliente = crear_cliente()
    print(f"Cliente: {cliente.nombre} {cliente.apellido}")


    opcion=0
    while opcion != 3:
        print(f" Numero de Cuenta: {cliente.numcuenta} con balance: {cliente.balance}")
        opcion=input("Escoger: Depositar (1), Retirar (2), o Salir (3)")
        print("escojio: "+str(opcion))
        if int(opcion)==1:

            cantidad=int(input("Cantidad a Depositar: "))
            cliente.depositar(cantidad)
        elif int(opcion) == 2:

            cantidad=int(input("Cantidad a Retirar: "))
            if cliente.balance>=cantidad:
                cliente.retirar(cantidad)
        elif int(opcion)==3:
            print("BYE")

inicio()


