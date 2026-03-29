import tkinter as tk

# CREAR VENTANA
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x450")
ventana.config(bg="#f5f5f5")

# FUNCIONES

# Añadir tarea
def añadir_tarea():
    tarea = entrada.get()
    if tarea != "":
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)

# Marcar como completada
def completar_tarea():
    try:
        indice = lista.curselection()[0]
        tarea = lista.get(indice)
        lista.delete(indice)
        lista.insert(indice, "✔ " + tarea)
    except:
        pass

# Eliminar tarea
def eliminar_tarea():
    try:
        indice = lista.curselection()[0]
        lista.delete(indice)
    except:
        pass

# Evento ENTER para agregar tarea
def evento_enter(event):
    añadir_tarea()

# Evento doble clic para completar
def doble_click(event):
    completar_tarea()

# COMPONENTES

titulo = tk.Label(
    ventana,
    text="📝 Lista de Tareas",
    font=("Arial", 16, "bold"),
    bg="#f5f5f5"
)
titulo.pack(pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Evento ENTER
entrada.bind("<Return>", evento_enter)

# BOTONES
frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=10)

btn_agregar = tk.Button(
    frame_botones,
    text="Añadir Tarea",
    bg="#4CAF50",
    fg="white",
    width=15,
    command=añadir_tarea
)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(
    frame_botones,
    text="Completar",
    bg="#2196F3",
    fg="white",
    width=15,
    command=completar_tarea
)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(
    frame_botones,
    text="Eliminar",
    bg="#f44336",
    fg="white",
    width=15,
    command=eliminar_tarea
)
btn_eliminar.grid(row=1, column=0, columnspan=2, pady=5)

# LISTA DE TAREAS
lista = tk.Listbox(ventana, width=40, height=15)
lista.pack(pady=20)

# Evento doble clic
lista.bind("<Double-Button-1>", doble_click)

# EJECUTAR

ventana.mainloop()