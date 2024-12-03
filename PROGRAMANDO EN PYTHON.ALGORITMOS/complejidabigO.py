import numpy as np
import time

# Crear una lista grande de números aleatorios
x = list(np.random.randint(low=1, high=500000, size=1000))  # Usa un tamaño menor para evitar problemas de memoria

# Definir la función
def constante(x: list) -> list:
    return x

# Medir el tiempo de ejecución con mayor precisión
start_time = time.perf_counter()
constante(x)
end_time = time.perf_counter()

# Imprimir el tiempo de ejecución en segundos (con precisión de nanosegundos)
print(f"Tiempo de ejecución: {(end_time - start_time) * 1e9} nanosegundos")
print(f"Tiempo de ejecución: {(end_time - start_time) * 1e6} microsegundos")

