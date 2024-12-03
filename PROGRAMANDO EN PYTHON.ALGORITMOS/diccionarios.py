#diccionarios El primer valor se trata de la clave y el segundo del valor asociado a la clave, clave:valorelimina los elemtos
dic = {
"Nombre":"Santiago",
"Apellido":"Hernandez",
"Pais":"España",
"Ciudad":"Madrid"
}
print(dic)

# Otra forma de definir diccionarios con la funcion dict()
dic2 = dict(
Nombre="Santiago",
Apellido="Hernandez",
Pais="España",
Ciudad="Madrid"
)
print(dic2)

#metodo clear eliminia los elementos del diccionario
mi_diccionario = {"nombre": "Juan", "edad": 25}
mi_diccionario.clear()
print(mi_diccionario) 

#metodo copy Devuelve una copia del diccionario, permitiendo modificar la copia sin afectar el original.
mi_diccionario = {"nombre": "Juan", "edad": 25}
diccionario2 = mi_diccionario.copy()
print(diccionario2) 

#metodo fromkeys() Crea un diccionario con claves especificadas y un valor común para todas.
claves = ["nombre", "edad", "ciudad"]
diccionario = dict.fromkeys(claves, "Desconocido")
print(diccionario) 

#metodo get() Obtiene el valor asociado a una clave. Devuelve None si la clave no existe, o un valor por defecto.
mi_diccionario = {"nombre": "Juan", "edad": 25}
print(mi_diccionario.get("nombre"))

#metodo items Devuelve una lista de tuplas donde cada tupla es un par clave-valor.
mi_diccionario = {"nombre": "Juan", "edad": 25}
print(mi_diccionario.items())

#metodo keys() Devuelve una lista de todas las claves del diccionario.
mi_diccionario = {"nombre": "Juan", "edad": 25}
print(mi_diccionario.keys())

#metodo pop() Elimina el par clave-valor de la clave especificada y devuelve su valor. Si la clave no existe, lanza un error.
mi_diccionario = {"nombre": "Juan", "edad": 25}
mi_diccionario.pop("nombre")
print(mi_diccionario)

#metodo popitem() Elimina y devuelve el último par clave-valor añadido.
mi_diccionario = {"nombre": "Juan", "edad": 25}
ultimo = mi_diccionario.popitem()
print(ultimo)
print(mi_diccionario)

#metodo setdefault() Devuelve el valor de una clave especificada. Si la clave no existe, la agrega con un valor dado.
mi_diccionario = {"nombre": "Juan", "edad": 25}
ultimo = mi_diccionario.setdefault("edad")
print(ultimo)
print(mi_diccionario)

#metodo update() Actualiza el diccionario con pares clave-valor de otro diccionario o de valores clave-valor específicos.
mi_diccionario = {"nombre": "Juan", "edad": 25}
mi_diccionario2 = {"direccion": "cobalto", "numero": 100}
mi_diccionario.update(mi_diccionario2)
mi_diccionario.update({"ciudad": "Madrid", "edad": 26})
print(mi_diccionario)     

#metodo values() Devuelve una lista con todos los valores del diccionario
mi_diccionario = {"nombre": "Juan", "edad": 25}
print(mi_diccionario.values())     


"""DICCIONARIO A PARTIR DE DOS LISTAS """
# Dos listas: una con nombres y otra con edades
nombres = ["Ana", "Juan", "Luis", "María"]
edades = [25, 30, 35, 28]

# Usamos zip para combinar ambas listas y luego dict para convertirlo en un diccionario
diccionario = dict(zip(nombres, edades))

print(diccionario)

"""Comprobar si una clave está en el diccionario"""
# Diccionario de ejemplo
mi_diccionario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Comprobar si la clave "edad" está en el diccionario
if "edad" in mi_diccionario:
    print("La clave 'edad' está en el diccionario")
else:
    print("La clave 'edad' no está en el diccionario")
    

"""Ejemplo de diccionario anidado"""
# Diccionario anidado de estudiantes
estudiantes = {
    "Juan": {
        "edad": 20,
        "materias": {
            "Matemáticas": 85,
            "Historia": 90,
            "Ciencias": 78
        }
    },
    "Ana": {
        "edad": 22,
        "materias": {
            "Matemáticas": 92,
            "Historia": 88,
            "Ciencias": 95
        }
    },
    "Luis": {
        "edad": 21,
        "materias": {
            "Matemáticas": 74,
            "Historia": 85,
            "Ciencias": 80
        }
    }
}

# Acceder a información dentro del diccionario anidado
print("Edad de Juan:", estudiantes["Juan"]["edad"])  # Salida: 20
print("Calificación de Ana en Ciencias:", estudiantes["Ana"]["materias"]["Ciencias"])  # Salida: 95
print("Calificación de Luis en Historia:", estudiantes["Luis"]["materias"]["Historia"])  # Salida: 85
