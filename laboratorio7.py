import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import math

def calcular_errores(Ti, Tr):
    n = len(Ti)

    # Calcular promedio de Tr
    STr = sum(Tr) / n

    # Calcular Ea
    Ea = [Tr[i] - STr for i in range(n)]

    # Calcular Ea2
    Ea2 = [ea ** 2 for ea in Ea]

    # Calcular sumatoria de Ea2
    SEa2 = sum(Ea2)

    # Calcular errores
    O2 = SEa2 / n                   # Valor medio cuadrático
    O = math.sqrt(O2)               # Desviación promedio
    ea = O / math.sqrt(n - 1)       # Error aleatorio
    er = ea / STr                   # Error relativo
    ep = er * 100                   # Error relativo porcentual

    return STr, Ea, Ea2, SEa2, O2, O, ea, er, ep

def obtener_datos():
    n = int(entry_n.get())
    Ti = []                 #Tiempo de reacción
    Tr = []                 #Tiempo de respuesta

    for i in range(n):
        Ti.append(float(entries_ti[i].get()))
        Tr.append(float(entries_tr[i].get()))

    return Ti, Tr

def calcular_y_mostrar_errores():
    Ti, Tr = obtener_datos()

    if len(Ti) != len(Tr):
        messagebox.showerror("Error", "La cantidad de datos de Ti y Tr no coincide.")
        return

    STr, Ea, Ea2, SEa2, O2, O, ea, er, ep = calcular_errores(Ti, Tr)

    resultado = f"""Promedio de Tr(Tiempo de respuesta): {STr}
Error absoluto (Ea): {Ea}
Error absoluto al cuadrado (Ea2): {Ea2}
Sumatoria de Error absoluto al cuadrado (Ea2): {SEa2}
Valor medio cuadrático (O2): {O2}
Desviación promedio (O): {O}
Error aleatorio (ea): {ea}
Error relativo (er): {er}
Error relativo porcentual (ep): {ep}"""

    messagebox.showinfo("Resultados", resultado)

# Crear la ventana principal
root = tk.Tk()
root.title("Cálculo de errores")

# Crear y colocar etiquetas y campos de texto para ingresar datos
label_n = tk.Label(root, text="Cantidad de datos:")
label_n.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1, padx=5, pady=5)

label_ti = tk.Label(root, text="Datos Ti:")
label_ti.grid(row=1, column=0, sticky="w", padx=5, pady=5)
label_tr = tk.Label(root, text="Datos Tr(resultado de Ti/estudiantes):")
label_tr.grid(row=1, column=1, sticky="w", padx=5, pady=5)

entries_ti = []
entries_tr = []

def agregar_campos():
    n = int(entry_n.get())
    for i in range(n):
        entry_ti = tk.Entry(root)
        entry_ti.grid(row=i+2, column=0, padx=5, pady=2)
        entries_ti.append(entry_ti)

        entry_tr = tk.Entry(root)
        entry_tr.grid(row=i+2, column=1, padx=5, pady=2)
        entries_tr.append(entry_tr)

button_agregar = tk.Button(root, text="Agregar campos", command=agregar_campos)
button_agregar.grid(row=0, column=2, padx=5, pady=5)

button_calcular = tk.Button(root, text="Calcular y mostrar errores", command=calcular_y_mostrar_errores)
button_calcular.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()