class Tarea:
    def __init__(self, titulo, descripcion, estado="Pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def completar(self):
        self.estado = "Completada"

    def __str__(self):
        return f"{self.titulo} - {self.estado}\nDescripción: {self.descripcion}"


class Dashboard:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        print("\n📋 DASHBOARD DE TAREAS - POO\n")
        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea}")

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completar()
            print("✅ Tarea marcada como completada")


# --- Uso del Dashboard ---
dashboard = Dashboard()

t1 = Tarea("Semana 08 - Dashboard", "poo")
t2 = Tarea("Principios SOLID", "tareas de poo")

dashboard.agregar_tarea(t1)
dashboard.agregar_tarea(t2)

dashboard.mostrar_tareas()
dashboard.completar_tarea(0)
dashboard.mostrar_tareas()
