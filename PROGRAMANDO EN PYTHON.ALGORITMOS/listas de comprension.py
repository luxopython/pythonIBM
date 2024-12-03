lista1 = [1,2,3,4,5,6,7]
print(lista1)

#lista2 tiene los valores (2*elemento) siendo elemento los valores de la lista1 multiplica por 2 los elementos de la lista1
lista2=[2*elemento for elemento in lista1]
print(lista2)

#crear una lista solo con los elementos pares
lista2 = [elemento for elemento in lista1 if elemento%2==0]
print(lista2)

#anidar iteraciones dentro de la lista La expresión elemento * elemento2 intenta multiplicar elemento 
# (un número) por elemento2 (una cadena de texto).
lista1 = [1,2,3,4,5,6,7]
lista2 = ["a","b","c","d","e","f","g"]
lista3 =[elemento*elemento2 for elemento in lista1 for elemento2 in lista2]
print(lista3)

#podemos poner incluso alguna condicion, multiplicara cuando elemento2 sea diferente de 2
lista3 =[elemento*elemento2 for elemento in lista1 for elemento2 in lista2 if elemento!=2]
print(lista3)

#Seleccion de elementos en una matriz o lista anidada  for row in lista4: este bucle itera sobre cada elemento de la
#lista 4, que en este caso son 3 listas
#row[1]: Accede al segundo elemento (índice 1, ya que los índices comienzan en 0) de la
# lista row. Esto selecciona el segundo elemento de cada sublista en lista4.

lista4 = [["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"]]
col2 = [row[1] for row in lista4]
print(col2)

#en este iteramos todos los elementos
lista4 = [["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"]]
col2 = [row for row in lista4 ]
print(col2)

lista4 = [["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"]]
col2 = [row[1] for row in lista4 if row[1] != "a2" ]
print(col2)

#COPIA PLANA Una copia plana crea una nueva colección que contiene referencias a los mismos elementos 
# que el objeto original. Si el objeto es una lista, diccionario o conjunto de listas (objetos compuestos), 
# solo se copiarán los "enlaces" al contenido original, no el contenido en sí. Si se modifica un elemento 
# mutable dentro de la copia, el cambio también se reflejará en el original.

import copy

# Creamos una lista compuesta con elementos mutables
original = [[1, 2, 3], [4, 5, 6]]

# Realizamos una copia plana
copia_plana = copy.copy(original)

# Modificamos un elemento dentro de la copia
copia_plana[0][0] = 'X'

print("Original:", original)        # La modificación afecta a `original`
print("Copia plana:", copia_plana)  # La modificación también está en `copia_plana`

"""COPIA PROFUNDA DEEP COPY  Una copia profunda crea una copia completamente independiente del objeto 
original y de todos sus subelementos, sin referencias al objeto original. Esto significa que cualquier 
cambio en los subelementos de la copia profunda no afectará al objeto original."""

import copy

# Creamos una lista compuesta con elementos mutables
original = [[1, 2, 3], [4, 5, 6]]

# Realizamos una copia profunda
copia_profunda = copy.deepcopy(original)

# Modificamos un elemento dentro de la copia
copia_profunda[0][0] = 'X'

print("Original:", original)         # No se ve afectado
print("Copia profunda:", copia_profunda)  # Solo la copia tiene la modificación
