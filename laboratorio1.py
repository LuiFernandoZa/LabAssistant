import tkinter as tk
import math
from tkinter import ttk
from openpyxl import Workbook
import os
def tratamientoEstadis():
    # Obtener datos ingresados
    datos = []
    for i in range(nroDatos):
        dato = {
            "Largo": float(entry_L[i].get()),
            "Ancho": float(entry_A[i].get()),
            "Altura": float(entry_H[i].get()),
            "Masa": float(entry_m[i].get())
        }
        datos.append(dato)
    
    # Calcular promedios
    promedios = {}
    for tipo in ["Largo", "Ancho", "Altura", "Masa"]:
        promedio = sum(dato[tipo] for dato in datos) / nroDatos
        promedios[tipo] = promedio
    
    # Calcular errores estándar
    errores_estandar = {}
    for tipo in ["Largo", "Ancho", "Altura", "Masa"]:
        suma_cuadrados = sum((dato[tipo] - promedios[tipo]) ** 2 for dato in datos)
        error_estandar = math.sqrt(suma_cuadrados / (nroDatos - 1))
        errores_estandar[tipo] = error_estandar
    
    # Calcular errores relativos
    errores_relativos = {}
    for tipo in ["Largo", "Ancho", "Altura", "Masa"]:
        error_relativo = 3 * errores_estandar[tipo] / promedios[tipo]
        errores_relativos[tipo] = error_relativo
    
    # Calcular volumen promedio y densidad promedio
    volumenProm = promedios["Largo"] * promedios["Ancho"] * promedios["Altura"]
    densidadProm = promedios["Masa"] / volumenProm
    
    # Calcular errores estándar y relativos para volumen y densidad
    error_estandar_volumen = math.sqrt(((errores_estandar["Largo"] ** 2) * ((promedios["Ancho"] * promedios["Altura"]) ** 2)) + 
                                  ((errores_estandar["Ancho"] ** 2) * ((promedios["Largo"] * promedios["Altura"]) ** 2)) + 
                                  ((errores_estandar["Altura"] ** 2) * ((promedios["Largo"] * promedios["Ancho"]) ** 2)))
    error_relativo_volumen = 3 * error_estandar_volumen / volumenProm
    
    error_estandar_densidad = math.sqrt(((errores_estandar["Masa"] ** 2) * ((1 / (promedios["Largo"] * promedios["Ancho"] * promedios["Altura"])) ** 2)) + 
                                  ((errores_estandar["Largo"] ** 2) * (((-1 * promedios["Masa"]) / (promedios["Largo"] ** 2 * promedios["Ancho"] * promedios["Altura"])) ** 2)) + 
                                  ((errores_estandar["Ancho"] ** 2) * (((-1 * promedios["Masa"]) / (promedios["Largo"] * promedios["Ancho"] ** 2 * promedios["Altura"])) ** 2)) + 
                                  ((errores_estandar["Altura"] ** 2) * (((-1 * promedios["Masa"]) / (promedios["Largo"] * promedios["Ancho"] * promedios["Altura"] ** 2)) ** 2)))
    error_relativo_densidad = 3 * error_estandar_densidad / densidadProm
    
    # Actualizar matriz con resultados
    matriz_resultados.delete(*matriz_resultados.get_children())  # Limpiar la matriz antes de actualizar
    for tipo in ["Largo", "Ancho", "Altura", "Masa"]:
        matriz_resultados.insert("", tk.END, values=[tipo, promedios[tipo], errores_estandar[tipo], errores_relativos[tipo] * 100])
    
    # Agregar resultados de volumen y densidad y sus errores si están disponibles
    matriz_resultados.insert("", tk.END, values=["Volumen", volumenProm, error_estandar_volumen, error_relativo_volumen * 100])
    matriz_resultados.insert("", tk.END, values=["Densidad", densidadProm, error_estandar_densidad, error_relativo_densidad * 100])
    
    # Exportar resultados a un archivo Excel
    wb = Workbook()
    ws = wb.active
    ws.append(["Tipo", "Promedio", "Error Estándar", "Error Relativo (%)"])
    for tipo in ["Largo", "Ancho", "Altura", "Masa"]:
        ws.append([tipo, promedios[tipo], errores_estandar[tipo], errores_relativos[tipo] * 100])
    ws.append(["Volumen", volumenProm, error_estandar_volumen, error_relativo_volumen * 100])
    ws.append(["Densidad", densidadProm, error_estandar_densidad, error_relativo_densidad * 100])
    wb.save("resultados.xlsx")  # Guardar el archivo como "resultados.xlsx"+
    os.startfile("resultados.xlsx")

def create_widgets():
    global nroDatos, entry_L, entry_A, entry_H, entry_m, matriz_resultados
    
    nroDatos = int(entry_nroDatos.get())
    
    # Crear entradas para los datos
    entry_L = [tk.Entry(root) for _ in range(nroDatos)]
    entry_A = [tk.Entry(root) for _ in range(nroDatos)]
    entry_H = [tk.Entry(root) for _ in range(nroDatos)]
    entry_m = [tk.Entry(root) for _ in range(nroDatos)]
    
    for i in range(nroDatos):
        tk.Label(root, text=f'Dato {i+1} Largo:').grid(row=2+i, column=0)  
        entry_L[i].grid(row=2+i, column=1)  
        tk.Label(root, text=f'Dato {i+1} Ancho:').grid(row=2+i, column=2)  
        entry_A[i].grid(row=2+i, column=3)  
        tk.Label(root, text=f'Dato {i+1} Altura:').grid(row=2+i, column=4)  
        entry_H[i].grid(row=2+i, column=5)  
        tk.Label(root, text=f'Dato {i+1} Masa:').grid(row=2+i, column=6)  
        entry_m[i].grid(row=2+i, column=7)  
    
    # Botón para realizar el cálculo
    calculate_button = tk.Button(root, text="Calcular", command=tratamientoEstadis)
    calculate_button.grid(row=nroDatos+3, column=0, columnspan=8)
    
    # Matriz para mostrar resultados
    matriz_resultados.grid(row=nroDatos+4, column=0, columnspan=8)

# Crear la ventana principal
root = tk.Tk()
root.title("Mediciones y cálculo de errores")

# Etiqueta y entrada para el número de datos
tk.Label(root, text="Número de datos:").grid(row=0, column=0)
entry_nroDatos = tk.Entry(root)
entry_nroDatos.grid(row=0, column=1)

# Botón para crear los widgets de entrada
create_button = tk.Button(root, text="Crear entradas", command=create_widgets)
create_button.grid(row=0, column=2)

# Crear matriz para mostrar resultados
matriz_resultados = ttk.Treeview(root, columns=("Tipo", "Promedio", "Error Estándar", "Error Relativo (%)"), show="headings")
matriz_resultados.heading("Tipo", text="Tipo")
matriz_resultados.heading("Promedio", text="Promedio")
matriz_resultados.heading("Error Estándar", text="Error Estándar")
matriz_resultados.heading("Error Relativo (%)", text="Error Relativo (%)")

root.mainloop()
