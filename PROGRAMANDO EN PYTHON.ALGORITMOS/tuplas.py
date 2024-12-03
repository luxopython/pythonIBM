tupla = (2, 3, 5, 6, "hola")
print (tupla[4])
#tupla.append(8) las tuplas no admiten añadir elementos una vez creadas para poder cambiarlas deberiamos 
                    #transformarlas en listas
                    
lista = list(tupla)
lista.append(8)
print(lista)

#recorrer una tupla elemento a elemento
thistuple =("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#comprobar si un elemeto esta en la tupla

thistuple =("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

#longitud de la tupla
thistuple =("apple", "banana", "cherry")
print(len(thistuple))

#unir dos tuplas.. deberiamos crear una tercera ya que no se pueden añadir ni quitar elementos
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#tambien existe el constructor tuple para poder crearla
thistuple = tuple(("apple", "banana", "cherry")) #note the double round-brackets
print(thistuple)

