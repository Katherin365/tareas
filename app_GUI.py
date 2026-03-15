import tkinter as tk
from tkinter import ttk

# Crear ventana principal

ventana = tk.Tk()
ventana.title("Gestor de Datos - Interfaz Gráfica")
ventana.geometry("450x400")
ventana.config(bg="#f6f0f7")

# FUNCIONES

def agregar_dato():
    dato = entrada.get()
    
    if dato != "":
        tabla.insert("", "end", values=(dato))
        entrada.delete(0, tk.END)

def limpiar_datos():
    for item in tabla.get_children():
        tabla.delete(item)

# ESTILO

style = ttk.Style()
style.theme_use("default")

# TITULO

titulo = tk.Label(
    ventana,
    text="Gestor de Datos",
    font=("Arial", 16, "bold"),
    bg="#f0f4f7",
    fg="#333"
)

titulo.pack(pady=15)

# FRAME DE ENTRADA
frame_entrada = tk.Frame(ventana, bg="#f0f4f7")
frame_entrada.pack(pady=10)

label = tk.Label(
    frame_entrada,
    text="Ingrese un dato:",
    font=("Arial", 11),
    bg="#f0f4f7"
)

label.grid(row=0, column=0, padx=5)

entrada = tk.Entry(frame_entrada, width=25)
entrada.grid(row=0, column=1, padx=5)

# BOTONES
frame_botones = tk.Frame(ventana, bg="#f0f4f7")
frame_botones.pack(pady=10)

boton_agregar = tk.Button(
    frame_botones,
    text="Agregar",
    width=12,
    bg="#4CAF50",
    fg="white",
    command=agregar_dato
)

boton_agregar.grid(row=0, column=0, padx=10)

boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    width=12,
    bg="#f44336",
    fg="white",
    command=limpiar_datos
)

boton_limpiar.grid(row=0, column=1, padx=10)

# TABLA DE DATOS

tabla = ttk.Treeview(ventana, columns=("Dato"), show="headings", height=10)
tabla.heading("Dato", text="Datos ingresados")
tabla.pack(pady=20)

# EJECUTAR APLICACIÓN

ventana.mainloop()