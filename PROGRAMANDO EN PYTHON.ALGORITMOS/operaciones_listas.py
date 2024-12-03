#metodo append agrega elemento al final de la lista
lista = [1, 2, 3]
lista.append(4)
print(lista)

# metodo clear borra los elementos de una lista
lista = [2,4,6,6]
print(lista)
lista.clear()
print("clear")
print(lista)

#metodo copy copia una lista en otra
lista = [2,4,6,6]
lista2 = lista.copy()
print(lista)
print("copy")
print(lista2)

#metodo count cuenta las veces que hay un elemento dentro de ua lista
lista = [2,4,6,6]
print("count")
print(lista.count(6))

#metodo extend agrega una lista al final de otra
lista = [2,4,6,6]
lista2 = [3,5,7,7]
lista.extend(lista2)
print("agregamos la lista 2 al final de la lista")
print(lista)

#metodo index devuelve el indice del elemento que indicamos epezamos por 0   0,1,2,3....
lista = [2,4,6,6]
print(lista.index(2))

#metodo insert añade un elemento en la posicion especificada
lista = [2,4,6,6]
print("agregamos hola en la posicion 3")
lista.insert(3,"hola")
print(lista)

#metodo pop borra el elemento en la posicion especificada y devuelve ese elemento, si no
#se especifica podicion borra el ultimo elemento
lista = [2,4,6,6]
print("borramos elemento 2")
elemento = lista.pop(2)
print(elemento)  
print(lista)

#metodo remove elimina el 1er elemento con el valor especificado
lista = [2,4,6,6]
print("borramos el primer 6 de la lista")
lista.remove(6) 
print(lista)

#metodo reverse invierte el orden de la lista
lista = [2,4,6,6]
print("invertimos de la lista")
lista.reverse()
print(lista)

#metodo sort ordena la lista en orden ascendente
lista = [5,3,4,1,2]
print("ordena la lista en ascendente")
lista.sort()
print(lista)

