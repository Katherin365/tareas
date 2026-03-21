import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesita instalar: pip install tkcalendar

# Clase principal de la aplicación

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # FRAME: Lista de eventos
      
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")

        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.pack()

        # FRAME: Entrada de datos
       
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        # Fecha
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1)

        # Hora
        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        # Descripción
        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = tk.Entry(frame_entrada)
        self.descripcion_entry.grid(row=2, column=1)

        # FRAME: Botones
       
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

    # Función para agregar evento
    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validación simple
        if fecha == "" or hora == "" or descripcion == "":
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        # Insertar en la tabla
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    # Función para eliminar evento
    
    def eliminar_evento(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Selecciona un evento para eliminar")
            return

        # Confirmación
        confirmacion = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
        if confirmacion:
            self.tree.delete(seleccionado)

# Ejecución del programa
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()