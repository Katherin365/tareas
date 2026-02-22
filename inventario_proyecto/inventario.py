from producto import Producto

class Inventario:
    """
    Clase que gestiona la lista de productos.
    """

    def __init__(self):
        self.productos = []  

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto si el ID no está repetido.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: El ID ya existe.")
                return

        self.productos.append(producto)
        print(" Producto añadido correctamente.")

   

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                print(" Producto eliminado correctamente.")
                return

        print(" Producto no encontrado.")

    

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:

                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)

                print(" Producto actualizado correctamente.")
                return

        print(" Producto no encontrado.")

    

    def buscar_por_nombre(self, nombre):
        encontrados = []

        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                encontrados.append(producto)

        if encontrados:
            print(" Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print(" No se encontraron productos con ese nombre.")

    

    def mostrar_productos(self):
        if not self.productos:
            print(" Inventario vacío.")
        else:
            print("\n Lista de productos:")
            for producto in self.productos:
                print(producto)