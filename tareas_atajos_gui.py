import tkinter as tk

# VENTANA PRINCIPAL

ventana = tk.Tk()
ventana.title("Gestor de Tareas con Atajos")
ventana.geometry("450x500")
ventana.config(bg="#f2f2f2")

# FUNCIONES

# Añadir tarea
def añadir_tarea(event=None):
    tarea = entrada.get()
    if tarea != "":
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)

# Marcar como completada
def completar_tarea(event=None):
    try:
        indice = lista.curselection()[0]
        tarea = lista.get(indice)

        # Evitar duplicar ✔
        if not tarea.startswith("✔"):
            lista.delete(indice)
            lista.insert(indice, "✔ " + tarea)
            lista.itemconfig(indice, {'fg': 'gray'})
    except:
        pass

# Eliminar tarea
def eliminar_tarea(event=None):
    try:
        indice = lista.curselection()[0]
        lista.delete(indice)
    except:
        pass

# Cerrar aplicación
def cerrar_app(event=None):
    ventana.destroy()

# INTERFAZ

titulo = tk.Label(
    ventana,
    text="📝 Lista de Tareas",
    font=("Arial", 16, "bold"),
    bg="#f2f2f2"
)
titulo.pack(pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# BOTONES

frame_botones = tk.Frame(ventana, bg="#f2f2f2")
frame_botones.pack(pady=10)

btn_agregar = tk.Button(
    frame_botones,
    text="Añadir",
    width=15,
    bg="#4CAF50",
    fg="white",
    command=añadir_tarea
)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(
    frame_botones,
    text="Completar",
    width=15,
    bg="#2196F3",
    fg="white",
    command=completar_tarea
)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(
    frame_botones,
    text="Eliminar",
    width=32,
    bg="#f44336",
    fg="white",
    command=eliminar_tarea
)
btn_eliminar.grid(row=1, column=0, columnspan=2, pady=5)

# LISTA

lista = tk.Listbox(ventana, width=40, height=15, font=("Arial", 10))
lista.pack(pady=20)

# ATAJOS DE TECLADO

# ENTER → añadir tarea
ventana.bind("<Return>", añadir_tarea)

# C → completar tarea
ventana.bind("c", completar_tarea)
ventana.bind("C", completar_tarea)

# DELETE → eliminar tarea
ventana.bind("<Delete>", eliminar_tarea)

# D → eliminar también
ventana.bind("d", eliminar_tarea)

# ESC → cerrar app
ventana.bind("<Escape>", cerrar_app)

# EJECUTAR

ventana.mainloop()
