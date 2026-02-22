from inventario import Inventario
from producto import Producto


def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)

            elif opcion == "2":
                id_producto = int(input("Ingrese el ID a eliminar: "))
                inventario.eliminar_producto(id_producto)

            elif opcion == "3":
                id_producto = int(input("Ingrese el ID a actualizar: "))
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))

                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "4":
                nombre = input("Ingrese el nombre a buscar: ")
                inventario.buscar_por_nombre(nombre)

            elif opcion == "5":
                inventario.mostrar_productos()

            elif opcion == "6":
                print(" Saliendo del sistema...")
                break

            else:
                print(" Opción inválida.")

        except ValueError:
            print(" Error: Entrada inválida. Verifique los datos numéricos.")


if __name__ == "__main__":
    menu()
