# Tiempo Promedio y Periodo
## Tiempo Promedio

def promedio(datos):
    if not datos: 
        return 0 
    else:
        promedio = sum(datos) / len(datos)
        return promedio

def ingresar_datos(numero_casos, elementos_por_casos):
    listas = [[] for _ in range(numero_casos)]

    for i in range(elementos_por_casos):
        for j in range(numero_casos):
            try:
                valor = float(input(f"Ingrese el tiempo {i + 1} para la caso {j + 1}: "))
                listas[j].append(valor)
            except ValueError:
                print("Error: Ingresa un valor numérico válido.")
                return None

    return listas

# Solicitar al usuario el número de listas y la cantidad de elementos por lista
numero_casos = int(input("Ingrese el número de casos analizados: "))
elementos_por_casos = int(input("Ingrese la cantidad de tiempos para cada caso: "))

# Llamar a la función para ingresar datos
datos_ingresados = ingresar_datos(numero_casos, elementos_por_casos)

# Listas para almacenar los resultados
promedios = []
periodos = []

# Calcular el promedio y el periodo para cada lista
for i, datos_lista in enumerate(datos_ingresados):
    tprom = promedio(datos_lista)
    periodo = tprom / 10
    print(f"Para el caso {i + 1} - Tiempo Promedio: {tprom:.4f}, Periodo: {periodo:.4f}")

    # Almacenar los resultados en las listas correspondientes
    promedios.append(tprom)
    periodos.append(periodo)

## Valores de x(bT^2), y(b^2), x^2(b^2T^4), y^2(b^4) y xy(b^3T^2)
def x(b, periodo):
    g = b*(periodo **2)
    g1 = round(g, 4)
    return g1 
def y(b):
    g = b**2
    g1 = round(g, 4)
    return g1
def x_cuadrado(b, periodo):
    g = (b*2)(periodo**4)
    g1 = round(g, 4)
    return g1 
def y_cuadrado(b):
    g = b**4
    g1 = round(g, 4)
    return g1
def xy(b, periodo):
    g = (b*3)(periodo**2)
    g1 = round(g, 4)
    return g1


b = [0.5, 0.45, 0.4, 0.35, 0.3, 0.28, 0.2, 0.15, 0.1]

resultados_x = []
resultados_y = []
resultados_x_cuadrado = []
resultados_y_cuadrado = []
resultados_xy = []

for valor_b in b:
    resultados_x.append(x(valor_b, periodo))
    resultados_y.append(y(valor_b))
    resultados_x_cuadrado.append(x_cuadrado(valor_b, periodo))
    resultados_y_cuadrado.append(y_cuadrado(valor_b))
    resultados_xy.append(xy(valor_b, periodo))


print(f"Resultados de x:", resultados_x)
print(f"Resultados de y:", resultados_y)
print(f"Resultados de x_cuadrado:", resultados_x_cuadrado)
print(f"Resultados de y_cuadrado:", resultados_y_cuadrado)
print(f"Resultados de xy:", resultados_xy)

# ## RESULTADOS ##
# ### Ecuación empirica y = ax + b###
# #### Determinando "a" ####


a1 = (len(b) * sum(resultados_xy)) - (sum(resultados_x) *sum(resultados_y)) / (len(b)*sum(resultados_x_cuadrado) - (sum(resultados_x)*2))
a = round(a1, 4)

# #### Determinando "b" ####


b1 = (sum(resultados_y) *sum(resultados_x_cuadrado))- (sum(resultados_x) * sum(resultados_xy)) / ((len(b) * sum(resultados_x_cuadrado)) - (sum(resultados_x)*2))
b = round(b1, 4)

# ## Determinando la ecuación y = ax + b ##
if b < 0: 
    print(f"Ecuación empírica y = F(x): {a}x {b}")
else: 
    print(f"Ecuación empírica y = F(x): {a}x +{b}")

# ### Radio de Giro K ###
import math 
B = b * -1
print(f"Radio de giro K: {math.sqrt(B):.4f}")

# ##### Aceleración de la gravedad #####

gravedad = (4 * (3.1416)**2) * a
print(f"Aceleración de gravedad: {gravedad:.4f}")

# ##### Momento de Inercia #####
masa = float(1.28)
I = masa * B
print(f"Momento de inercia: {I:.4f}")