import json

# CLASE PRODUCTO

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

  
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }



# CLASE INVENTARIO

class Inventario:
    def __init__(self):
    
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print(" El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print(" Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(" Producto eliminado.")
        else:
            print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print(" Producto actualizado.")
        else:
            print(" Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            producto for producto in self.productos.values()
            if producto.get_nombre().lower() == nombre.lower()
        ]
        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print(" Inventario vacío.")
            return

        print("\n===== INVENTARIO PAPELERÍA =====")
        for producto in self.productos.values():
            print(f"ID: {producto.get_id()}")
            print(f"Nombre: {producto.get_nombre()}")
            print(f"Cantidad: {producto.get_cantidad()}")
            print(f"Precio: ${producto.get_precio():.2f}")
            print("------------------------------")

    def valor_total(self):
        total = 0
        for producto in self.productos.values():
            total += producto.get_cantidad() * producto.get_precio()
        return total

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            datos = [producto.to_dict() for producto in self.productos.values()]
            json.dump(datos, archivo)
        print(" Inventario guardado correctamente.")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    producto = Producto(
                        item["id"],
                        item["nombre"],
                        item["cantidad"],
                        item["precio"]
                    )
                    self.productos[item["id"]] = producto
            print(" Inventario cargado correctamente.")
        except FileNotFoundError:
            print(" No existe archivo previo. Se creará uno nuevo.")


def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario_papeleria.json")

    if not inventario.productos:
        productos_iniciales = [
            Producto("P001", "Cuaderno Universitario", 50, 2.50),
            Producto("P002", "Lapiz HB", 200, 0.25),
            Producto("P003", "Borrador Blanco", 150, 0.30),
            Producto("P004", "Esfero Azul", 180, 0.50),
            Producto("P005", "Resaltador Amarillo", 60, 0.75)
        ]
        for p in productos_iniciales:
            inventario.añadir_producto(p)

    while True:
        print("\n=== SISTEMA DE INVENTARIO - PAPELERÍA ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos")
        print("6. Mostrar valor total del inventario")
        print("7. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto.to_dict())
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print(f" Valor total del inventario: ${inventario.valor_total():.2f}")

        elif opcion == "7":
            inventario.guardar_en_archivo("inventario_papeleria.json")
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    menu()
