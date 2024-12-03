#1. Dados dos números, escriba un código Python para encontrar el mínimo de estos dos números
a = 2
b = 4
print(min(a,b))


#2. Invertir palabras de una cadena dada.
str3 = ""                       
str = "codigo de prueba"
str2=str.split(" ")         #partimos la cadena con split y queda en str2
print(str2)

str3=" ".join(reversed(str2)) #en str3 las juntamos con join reversed
print(str3)

#3. Realizar una suma de los elementos de una tupla
suma=0
mytupla = (1,2,3,4)
for k in mytupla:
    print(suma)
    suma = suma + k
print(suma)
        

#4. Escriba un código que calcule una lista de números proporcionados
def suma_numeros(numeros):
    if len(numeros) == 0:
        return print("esta vacio")
    elif len(numeros) == 1:
        return print(sum(numeros))
    else:
        return print(sum(numeros))
    
numeros = [2]
suma_numeros(numeros)

#5. Escriba un código que desordene al azar una lista.
from random import shuffle
lista = [1, 2, "los", "dos"]
shuffle(lista)
print(lista)

#6. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.

def contar_palabras_mayusculas(nombre_archivo):
    # Contador para palabras en mayúsculas
    contador_mayusculas = 0

    # Abrimos el archivo en modo de lectura
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # Dividimos la línea en palabras
            palabras = linea.split()
            for palabra in palabras:
                # Comprobamos si la palabra está completamente en mayúsculas
                if palabra.isupper():
                    contador_mayusculas += 1

    return contador_mayusculas

# Ejemplo de uso:
nombre_archivo = 'C:/Users/kaesh/OneDrive/Escritorio/CURSO PYTHON IBM/MODULO 2 FASE FORMACION Y EJERCICIOS PYTHON/PRACTICAS PYTHON/TEST1/archivo_texto.txt'
  # Reemplaza con el nombre de tu archivo
resultado = contar_palabras_mayusculas(nombre_archivo)
print(f'Número de palabras en mayúsculas: {resultado}')


#Recorrer una lista a la inversa

mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista[::-1]:
    print(elemento)
