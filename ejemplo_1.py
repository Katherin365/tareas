# Programa: Sistema de Reservas de Habitaciones
# Descripción: Ejemplo del mundo real aplicando Programación Orientada a Objetos (POO)

# Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        self.disponible = False

    def mostrar_info(self):
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Precio: ${self.precio}"


# Clase que representa a un cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_info(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula}"


# Clase que representa una reserva
class Reserva:
    def __init__(self, cliente, habitacion, fecha):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha = fecha

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.reservar()
            print("Reserva confirmada con éxito")
        else:
            print("La habitación no está disponible")

    def mostrar_reserva(self):
        print(self.cliente.mostrar_info())
        print(self.habitacion.mostrar_info())
        print(f"Fecha de reserva: {self.fecha}")


# ----- Uso del sistema -----

# Creación de objetos
habitacion1 = Habitacion(101, "Simple", 50)
cliente1 = Cliente("Ana Pérez", "0102030405")

# Creación de una reserva
reserva1 = Reserva(cliente1, habitacion1, "2025-01-15")

# Confirmar y mostrar reserva
reserva1.confirmar_reserva()
reserva1.mostrar_reserva()
