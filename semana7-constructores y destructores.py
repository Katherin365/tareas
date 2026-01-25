
class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.
    Demuestra el uso de constructores (__init__) y destructores (__del__).
    """

    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor de la clase.
        Se llama automáticamente al crear un objeto.
        Inicializa los atributos titular y saldo.
        """
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Cuenta creada para {self.titular} con saldo inicial de ${self.saldo}.")

    def depositar(self, monto):
        """
        Método para depositar dinero en la cuenta.
        """
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto} realizado. Saldo actual: ${self.saldo}.")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        """
        Método para retirar dinero de la cuenta.
        """
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto} realizado. Saldo actual: ${self.saldo}.")
        else:
            print("Fondos insuficientes o monto inválido.")

    def __del__(self):
        """
        Destructor de la clase.
        Se llama automáticamente cuando el objeto es destruido.
        Aquí se puede hacer limpieza de recursos.
        """
        print(f"La cuenta de {self.titular} está siendo eliminada. Saldo final: ${self.saldo}.")


if __name__ == "__main__":
    
    cuenta1 = CuentaBancaria("Kat Neppas", 500)
    cuenta2 = CuentaBancaria("Juan Pérez")

    cuenta1.depositar(200)
    cuenta1.retirar(100)

    cuenta2.depositar(1000)
    cuenta2.retirar(500)

    print("Fin del programa.")
