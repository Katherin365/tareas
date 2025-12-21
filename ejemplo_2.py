# Programa: Sistema de Biblioteca
# Ejemplo del mundo real aplicando Programación Orientada a Objetos (POO)

# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar_libro(self):
        self.disponible = False

    def mostrar_info(self):
        return f"Libro: {self.titulo} | Autor: {self.autor}"


# Clase que representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def mostrar_info(self):
        return f"Usuario: {self.nombre} | Código: {self.codigo}"


# Clase que representa un préstamo
class Prestamo:
    def __init__(self, usuario, libro, fecha):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha

    def realizar_prestamo(self):
        if self.libro.disponible:
            self.libro.prestar_libro()
            print("Préstamo realizado con éxito")
        else:
            print("El libro no está disponible")

    def mostrar_prestamo(self):
        print(self.usuario.mostrar_info())
        print(self.libro.mostrar_info())
        print(f"Fecha del préstamo: {self.fecha}")


# ----- Uso del sistema -----

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
usuario1 = Usuario("Carlos López", "U123")

prestamo1 = Prestamo(usuario1, libro1, "2025-01-20")

prestamo1.realizar_prestamo()
prestamo1.mostrar_prestamo()
