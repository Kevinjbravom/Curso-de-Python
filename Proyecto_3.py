class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo=0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad}$ en la cuenta.")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > 0 and self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}$ de la cuenta.")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def transferir(self, otra_cuenta, cantidad):
        if cantidad > 0 and self.saldo >= cantidad:
            self.saldo -= cantidad
            otra_cuenta.saldo += cantidad
            print(f"Se han transferido {cantidad}$ a la cuenta de {otra_cuenta.titular}.")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def mostrar_saldo(self):
        print(f"El sal(do actual de la cuenta de {self.titular} es: {self.saldo}$.")

def mostrar_menu():
    print("")
    print("****** Menú de Opciones ******")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Transferir")
    print("4. Mostrar Saldo")
    print("5. Salir")
    print("")

class Cuenta:
    def __init__(self):
        self.titular = input("Ingrese el nombre del titular de la cuenta: ")
        self.numero_cuenta = input("Ingrese el número de cuenta (12 dígitos): ")
        while len(self.numero_cuenta) != 12:
            print("El número de cuenta debe tener exactamente 12 dígitos. Inténtelo de nuevo.")
            self.numero_cuenta = input("Ingrese el número de cuenta (12 dígitos): ")
        self.cuenta_bancaria = CuentaBancaria(self.titular, self.numero_cuenta)

    def acceder_menu(self):
        opcion = 0
        while opcion != 5:
            mostrar_menu()
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                self.cuenta_bancaria.depositar(cantidad)
            elif opcion == 2:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                self.cuenta_bancaria.retirar(cantidad)
            elif opcion == 3:
                cantidad = float(input("Ingrese la cantidad a transferir: "))
                cuenta_destino = input("Ingrese el titular de la cuenta destino: ")
                otra_cuenta = CuentaBancaria(cuenta_destino, "0000")
                self.cuenta_bancaria.transferir(otra_cuenta, cantidad)
            elif opcion == 4:
                self.cuenta_bancaria.mostrar_saldo()
            elif opcion == 5:
                print("Saliendo del programa...")
            else:
                print("Opción inválida. Intente de nuevo.")


cuenta = Cuenta()
cuenta.acceder_menu()

