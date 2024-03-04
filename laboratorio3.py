import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy import stats

def calcular_w(m):
    """
    Calcula el valor de W a partir de la masa (m).

    Args:
        m (float): La masa del objeto en kilogramos.

    Returns:
        float: El valor de W.
    """
    g = 9.81  # Aceleración gravitatoria
    return m * g

def calcular_us(fs, w):
    """
    Calcula el valor de Us a partir de Fs y W.

    Args:
        fs (float): El valor de Fs.
        w (float): El valor de W.

    Returns:
        float: El valor de Us.
    """
    return fs / w

def calcular_uk(fk, w):
    """
    Calcula el valor de Uk a partir de Fk y W.

    Args:
        fk (float): El valor de Fk.
        w (float): El valor de W.

    Returns:
        float: El valor de Uk.
    """
    return fk / w

def agregar_valores():
    """
    Agrega un nuevo conjunto de entradas para M, Fs y Fk.
    """
    global frame_entradas, contador_filas, entries

    contador_filas += 1
    entry_m = tk.Entry(frame_entradas)
    entry_m.grid(row=contador_filas, column=0)

    entry_fs1 = tk.Entry(frame_entradas)
    entry_fs1.grid(row=contador_filas, column=1)

    entry_fs2 = tk.Entry(frame_entradas)
    entry_fs2.grid(row=contador_filas, column=2)

    entry_fk1 = tk.Entry(frame_entradas)
    entry_fk1.grid(row=contador_filas, column=3)

    entry_fk2 = tk.Entry(frame_entradas)
    entry_fk2.grid(row=contador_filas, column=4)

    entries.append((entry_m, entry_fs1, entry_fs2, entry_fk1, entry_fk2))

def actualizar_tabla_w():
    """
    Actualiza la tabla W con los nuevos datos y crea el gráfico de dispersión.
    """
    global tabla_w, entries
    try:
        # Limpiar la tabla
        tabla_w.delete(*tabla_w.get_children())

        # Listas para almacenar los datos de W y Fsp
        w_values = []
        fsp_values = []

        for entry_m, entry_fs1, entry_fs2, entry_fk1, entry_fk2 in entries:
            m = float(entry_m.get())
            fs1 = float(entry_fs1.get())
            fs2 = float(entry_fs2.get())
            fk1 = float(entry_fk1.get())
            fk2 = float(entry_fk2.get())

            # Calcular promedio de Fs1 y Fs2 (fsp) y de Fk1 y Fk2 (fkp)
            fsp = (fs1 + fs2) / 2
            fkp = (fk1 + fk2) / 2

            # Calcular W
            w = calcular_w(m)
            us = calcular_us(fsp, w)
            uk = calcular_uk(fkp, w)

            # Agregar valores a las listas
            w_values.append(w)
            fsp_values.append(fsp)

            # Actualizar valores en la tabla para cada masa
            tabla_w.insert("", tk.END, values=(m, "{:.4f}".format(w), "{:.4f}".format(fsp), "{:.4f}".format(fkp), "{:.4f}".format(us), "{:.4f}".format(uk)))

        # Calcular la línea de tendencia lineal
        slope, intercept, r_value, p_value, std_err = stats.linregress(w_values, fsp_values)
        line = [slope * w + intercept for w in w_values]

        # Crear una ventana de matplotlib y asignarla a la ventana principal de Tkinter
        fig, ax = plt.subplots()
        ax.scatter(w_values, fsp_values, label='Datos')
        ax.plot(w_values, line, color='red', label='Línea de tendencia')
        ax.set_xlabel('W (N)')
        ax.set_ylabel('Fsp')
        ax.set_title('Gráfico de dispersión de W vs Fsp')
        ax.grid(True)
        ax.legend()
        plt.show()

    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

def main():
    """
    Función principal del programa.
    """
    global frame_entradas, tabla_w, entries, contador_filas

    # Crear ventana
    window = tk.Tk()
    window.title("Rozamiento")

    # Crear marco para las entradas
    frame_entradas = tk.Frame(window)
    frame_entradas.pack()

    # Etiquetas para M, Fs y Fk
    label_m = tk.Label(frame_entradas, text="Masa (kg)")
    label_m.grid(row=0, column=0)

    label_fs1 = tk.Label(frame_entradas, text="Fs1 (N)")
    label_fs1.grid(row=0, column=1)

    label_fs2 = tk.Label(frame_entradas, text="Fs2 (N)")
    label_fs2.grid(row=0, column=2)

    label_fk1 = tk.Label(frame_entradas, text="Fk1 (N)")
    label_fk1.grid(row=0, column=3)

    label_fk2 = tk.Label(frame_entradas, text="Fk2 (N)")
    label_fk2.grid(row=0, column=4)

    # Botón para agregar valores
    button_agregar = tk.Button(window, text="Agregar valores", command=agregar_valores)
    button_agregar.pack()

    # Botón para actualizar la tabla W
    button_actualizar = tk.Button(window, text="Resultado", command=actualizar_tabla_w)
    button_actualizar.pack()

    # Tabla para mostrar los datos de M, W y Fsp
    tabla_w = ttk.Treeview(window, columns=("Masa (kg)", "W (N)", "Fsp", "Fkp", "Us", "Uk"))
    tabla_w.heading("#0", text="")
    tabla_w.column("#0", width=0, minwidth=0, stretch=False)
    tabla_w.heading("Masa (kg)", text="Masa (kg)")
    tabla_w.column("Masa (kg)", width=100, minwidth=100, stretch=False)
    tabla_w.heading("W (N)", text="W (N)")
    tabla_w.column("W (N)", width=100, minwidth=100, stretch=False)
    tabla_w.heading("Fsp", text="Fsp")
    tabla_w.column("Fsp", width=100, minwidth=100, stretch=False)
    tabla_w.heading("Fkp", text="Fk promedio")
    tabla_w.column("Fkp", width=100, minwidth=100, stretch=False)
    tabla_w.heading("Us", text="Us")
    tabla_w.column("Us", width=100, minwidth=100, stretch=False)
    tabla_w.heading("Uk", text="Uk")
    tabla_w.column("Uk", width=100, minwidth=100, stretch=False)
    tabla_w.pack()

    # Inicializar variables
    entries = []  # Lista para almacenar las entradas
    contador_filas = 0  # Contador de filas

    window.mainloop()

if __name__ == "__main__":
    main()








