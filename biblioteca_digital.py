# CLASE LIBRO


class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para almacenar título y autor 
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False

    def __str__(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# CLASE USUARIO


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        
        # Lista para libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self.libros_prestados:
                print(libro)


# CLASE BIBLIOTECA


class Biblioteca:

    def __init__(self):
        # Diccionario para almacenar libros por ISBN
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Conjunto para IDs únicos
        self.ids_usuarios = set()


    # GESTIÓN DE LIBROS
    

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro añadido correctamente")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # GESTIÓN DE USUARIOS
   

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("ID de usuario ya existe")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")


    # PRÉSTAMOS
    

    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no existe")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro.prestado:
            print("El libro ya está prestado")
        else:
            libro.prestado = True
            usuario.prestar_libro(libro)
            print("Libro prestado correctamente")


    def devolver_libro(self, isbn, id_usuario):

        if isbn not in self.libros or id_usuario not in self.usuarios:
            print("Datos incorrectos")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro in usuario.libros_prestados:
            usuario.devolver_libro(libro)
            libro.prestado = False
            print("Libro devuelto correctamente")
        else:
            print("El usuario no tiene ese libro")


    # BÚSQUEDAS
    

    def buscar_titulo(self, titulo):
        for libro in self.libros.values():
            if libro.info[0].lower() == titulo.lower():
                print(libro)

    def buscar_autor(self, autor):
        for libro in self.libros.values():
            if libro.info[1].lower() == autor.lower():
                print(libro)

    def buscar_categoria(self, categoria):
        for libro in self.libros.values():
            if libro.categoria.lower() == categoria.lower():
                print(libro)


# PRUEBAS DEL SISTEMA

biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel Garcia Marquez", "Novela", "111")
libro2 = Libro("1984", "George Orwell", "Distopía", "222")
libro3 = Libro("Python Básico", "Juan Perez", "Programación", "333")

# Añadir libros
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Ana", "U01")
usuario2 = Usuario("Luis", "U02")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("111", "U01")

# Mostrar libros del usuario
print("\nLibros prestados a Ana:")
usuario1.listar_libros()

# Devolver libro
biblioteca.devolver_libro("111", "U01")

# Buscar libro
print("\nBusqueda por autor:")
biblioteca.buscar_autor("George Orwell")