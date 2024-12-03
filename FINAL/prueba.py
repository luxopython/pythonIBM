"""     Ejercicio Final Luciano.ga.al@gmail.com
        Programa Gestion de Stock  no permite 6 opciones
        1 Agregar producto                 
        2 Modificar precio a un producto   
        3 Eliminar producto                     
        4 Buscar producto                     
        5 Resumen inventario                 
    Contiene 2 clases (Producto e Inventario) y la funcion ingresar_nombre()
"""

class Producto():   #definimos la clase Producto
    
    def __init__(self, nombre, categoria, precio, cantidad): #constructor de la clase con 4 parametros
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad
        
 #definimos los setters y los getters de los atributos de la clase Producto
        
    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_nombre(self):
        return self._nombre
    
    def set_categoria(self, categoria):
        self._categoria = categoria
        
    def get_categoria(self):
        return self._categoria
    
    def set_precio(self, precio):
        self._precio = precio
        
    def get_precio(self):
        return self._precio
  
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad
        
    def get_cantidad(self):
        return self._cantidad     

class Inventario(): #definimos la clase Inventario
    
    def __init__(self):         #constructor de la clase que es una lista vacia que luego iremos llenando de productos
        self.inventario = []
        
#metodo agregar_producto que nos pide un nombre_m que le daremos previa llamada a funcion ingresar_nombre que devuelve 
# un nombre (return nombre) que recogemos en el parametro que le pasamos nombre_m, con el try except controlamos que
#el valos de precio y cantidad sean numeros y con el if > 0 que sean numeros mayores a 0      

    def agregar_producto(self,nombre_m):    
        nombre = nombre_m                                  
        categoria = (input("A que categoria de productos pertenece?: ")) 

        while True:
            try:
                precio = int(input("Escribe un precio que sea mayor que 0: "))
                if precio > 0:
                    break
                else:
                    print("El precio debe ser mayor que 0.")
            except ValueError:
                print("Debes poner un precio mayor que 0")
                
        while True:
            try:
                cantidad = int(input("Escribe una cantidad de productos mayor que 0: "))
                if cantidad > 0:
                    break
                else:
                    print("la cantidad debe ser mayor que 0.")
            except ValueError:
                print("Debes poner una cantidad mayor que 0")           
        
        
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
                print("Debes poner un precio mayor que 0")
                
         
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
            
#creamos la funcion ingresar nombre ya que la usaremos recurrentemente retorna el nombre que ingresamos por teclado 
       
def ingresar_nombre(): 
    nombre = (input("Escriba el nombre del producto: "))
    return nombre

if __name__ == "__main__":
    supermercado = Inventario()  # Creamos el objeto supermercado una instancia de la clase Inventario

    escoger = 100  # le damos un valor 100 a escoger para que podamos entrar al bucle while
    while escoger != 0:
        while True:  # imprimimos y damos al usuario opción del 0 al 5 para moverse entre el menú
            try:  # controlamos lo ingresado con el try que sea valor numérico y con el if que sean entre el 0 y 5
                print("***************************************")
                print("*           Gestion de Stock          *")
                print("* 1 Agregar producto                  *")
                print("* 2 Modificar precio a un producto    *")
                print("* 3 Eliminar producto                 *")
                print("* 4 Buscar producto                   *")
                print("* 5 Resumen inventario                *")
                escoger = int(input("* 0 Salir Gestion de Stock            * : "))
                if 0 <= escoger <= 5:
                    break
                else:
                    print("Error Debe ser una opción entre 0 y 5 ")
            except ValueError:
                print("ERROR Debe ser una opción entre 0 y 5 ")

        if escoger == 1:  # si elige 1
            nombre_m = ingresar_nombre()  # pedimos nombre
            si_esta = supermercado.buscar_producto(nombre_m)  # buscar_producto devuelve True si nombre_m está en nuestra lista
            if si_esta != True:
                supermercado.agregar_producto(nombre_m)
            else:
                print("El nombre del producto ya existe, no pueden existir nombres duplicados")
        elif escoger == 2:
            nombre_m = ingresar_nombre()
            si_esta = supermercado.buscar_producto(nombre_m)
            if si_esta == True:
                supermercado.modificar_precio(nombre_m)
        elif escoger == 3:
            nombre_m = ingresar_nombre()
            si_esta = supermercado.buscar_producto(nombre_m)
            if si_esta == True:
                supermercado.eliminar_producto(nombre_m)
        elif escoger == 4:
            nombre_m = ingresar_nombre()
            si_esta = supermercado.buscar_producto(nombre_m)
            if si_esta == True:
                supermercado.buscar_producto_nombre(nombre_m)
        elif escoger == 5:
            supermercado.listar_inventario()
        elif escoger == 0:
            print("Adiós")
            break
        else:
            print("Opción inválida, pulsa un número entre 0 y 5")
