import os

class Producto_papeleria:
    """
    Clase que representa un producto del inventario.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


class Inventario:
    
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = ["lapiz", "cuaderno", "regla", "goma", "tijeras"]
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
       
        try:
            if not os.path.exists(self.archivo):
                # Si el archivo no existe, lo crea vacío
                open(self.archivo, "w").close()
                print(" Archivo de inventario creado.")

            with open(self.archivo, "r") as file:
                for linea in file:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(
                            int(id_producto),
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                        self.productos.append(producto)
                    except ValueError:
                        print(" Línea corrupta ignorada:", linea.strip())

            print("Inventario cargado correctamente.")

        except PermissionError:
            print(" Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(" Error inesperado al cargar el archivo:", e)

    def guardar_en_archivo(self):
        """
        Guarda todos los productos en el archivo.
        """
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")

            print(" Inventario guardado correctamente.")

        except PermissionError:
            print(" Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(" Error inesperado al guardar:", e)

    def añadir_producto(self, producto):
        self.productos.append(producto)
        self.guardar_en_archivo()
        print(" Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id == id_producto:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print(" Producto eliminado correctamente.")
                return
        print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.id == id_producto:
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio

                self.guardar_en_archivo()
                print(" Producto actualizado correctamente.")
                return
        print(" Producto no encontrado.")

    def mostrar_productos(self):
        if not self.productos:
            print(" Inventario vacío.")
        else:
            for producto in self.productos:
                print(producto)



def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Mostrar productos")
        print("2. Añadir producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                inventario.mostrar_productos()

            elif opcion == "2":
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == "3":
                id_producto = int(input("ID del producto a actualizar: "))
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "4":
                id_producto = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)

            elif opcion == "5":
                print(" Saliendo del sistema...")
                break

            else:
                print(" Error: Opción inválida.")

        except ValueError:
            print(" Error: Entrada inválida. Verifica los datos numéricos.")
        except Exception as e:
            print(" Error inesperado:", e)


if __name__ == "__main__":
    menu()