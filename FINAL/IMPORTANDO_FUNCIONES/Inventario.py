from Producto import Producto

class Inventario(): #definimos la clase Inventario
    
    def __init__(self):         #constructor de la clase que es una lista vacia que luego iremos llenando de productos
        self.inventario = []
        
#metodo agregar_producto que nos pide un nombre_m que le daremos previa llamada a funcion ingresar_nombre que devuelve 
# un nombre (return nombre) que recogemos en el parametro que le pasamos nombre_m, con el try except controlamos que
#el valos de precio y cantidad sean numeros y con el if > 0 que sean numeros mayores a 0      

    def agregar_producto(self,nombre_m):    
     
        while True:
            if nombre_m == "":
                nombre_m = input("no puedes dejar el nombre en blanco, vuelve a intentarlo: ")
            else:
                nombre = nombre_m  
                break

        categoria = (input("A que categoria de productos pertenece?: "))   
        while True:
            if categoria == "":
                categoria = input("no puedes dejar la categoria en blanco, vuelve a intentarlo: ")
            else:
 
                break
        while True:
            try:
                precio = int(input("Escribe un precio que sea mayor que 0: "))
                if precio > 0:
                    break
                else:
                    print("El precio debe ser mayor que 0.")
            except ValueError:
                print("No puedes dejarlo en blanco poner letras o un numero menor de 0")
                
        while True:
            try:
                cantidad = int(input("Escribe una cantidad de productos mayor o igual que 0: "))
                if cantidad >= 0:
                    break
                else:
                    print("la cantidad debe ser mayor que 0.")
            except ValueError:
                print("No puedes dejarlo en blanco poner letras o un numero menor de 0")           
        
        
        producto = Producto(nombre, categoria, precio, cantidad)    #una vez validadas las entradas creamos la instancia        
        self.inventario.append(producto)                            #y la agregamos a la lista

#metodo buscar_producto que nos pide un nombre_m que le daremos previa llamada a funcion ingresar_nombre que devuelve 
# un nombre (return nombre) que recogemos en el parametro que le pasamos nombre_m, con el for buscamos en la lista inventario
# y si hay un nombre de producto que coincide con el que hemos pasado decimos que si esta en la lista y devolvemos true
      
    def buscar_producto(self,nombre_m):
        esta = False
        for producto in self.inventario:
            if producto.get_nombre() == nombre_m:
                esta = True
                break
            else:
                esta = False
                
        if esta == True:
            print("El producto SI esta en la lista")
            return True
        else:
            print("El producto NO esta en la lista")
            return False   
 
#metodo modificar_precio que nos pide un nombre_m que le daremos previa llamada a funcion ingresar_nombre que devuelve 
# un nombre (return nombre) que recogemos en el parametro que le pasamos nombre_m, (antes hemos buscado si el nombre existia)
#fuera de este metodo con la funcion buscar_producto, si existe ya vamos a modificar precio que controlamos que sea un numero 
#con el try except y que sea mayor que 0 con el if precio_m > 0 que previamente habremos ingresado por teclado (precio_m)
        
    def modificar_precio(self,nombre_m):
   
        while True:
            try:
                precio_m = int(input("Escribe un precio que sea mayor que 0: "))
                if precio_m > 0:
                    break
                else:
                    print("El precio debe ser mayor que 0.")
            except ValueError:
                print("Debes poner un precio mayor que 0 y no letras")
                
         
        for producto in self.inventario:    #miramos que nombre coincide de la lista inventario y modificamos el parametro precio
            if producto.get_nombre() == nombre_m:
                producto.set_precio(precio_m)
                print(F"Has modificado el precio de {nombre_m}")
                break

#metodo eliminar_producto que nos pide un nombre_m que le daremos previa llamada a funcion ingresar_nombre que devuelve 
# un nombre (return nombre) que recogemos en el parametro que le pasamos nombre_m, (antes hemos buscado si el nombre existia)
#fuera de este metodo con la funcion buscar_producto, si existe eliminamos el producto 
# coincidente con el nombre self.inventario.remove
              
    def eliminar_producto(self,nombre_m):              
        for producto in self.inventario:
            if producto.get_nombre() == nombre_m:
                self.inventario.remove(producto)
                print(F"Has eliminado {nombre_m}")
                break

 #metodo buscar_producto_nombre que nos pide un nombre_m que le daremos previa llamada a funcion ingresar_nombre que devuelve 
# un nombre (return nombre) que recogemos en el parametro que le pasamos nombre_m, (antes hemos buscado si el nombre existia)
#fuera de este metodo con la funcion buscar_producto, si el nombre del producto existe imprimmos sus parametros

    def buscar_producto_nombre(self,nombre_m):              
        for producto in self.inventario:
            if producto.get_nombre() == nombre_m:
                print(f"Nombre: {producto.get_nombre()}")
                print(f"Categoría: {producto.get_categoria()}")
                print(f"Precio: {producto.get_precio()}")
                print(f"Cantidad: {producto.get_cantidad()}")
                print("*****************************")
            else:
                print("El producto no esta en la lista")
                
 #metodo listar_inventario primero miramos que la lista no este vacia con el metodo len de las listas y 
 # con el for recorremos cada producto de la lista inventario e imprimimos sus parametros

    def listar_inventario(self):
        if len(self.inventario) == 0:
            print("El inventario esta vacio")
        else:
            for producto in self.inventario:
                print(f"Nombre: {producto.get_nombre()}")
                print(f"Categoría: {producto.get_categoria()}")
                print(f"Precio: {producto.get_precio()}")
                print(f"Cantidad: {producto.get_cantidad()}")
                print("*****************************")