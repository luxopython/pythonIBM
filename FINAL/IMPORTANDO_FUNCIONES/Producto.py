class Producto():   #definimos la clase Producto
    
    def __init__(self, nombre, categoria, precio, cantidad): #constructor de la clase con 4 parametros
        self.__nombre = nombre                          
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad
        
 #definimos los setters y los getters de los atributos de la clase Producto
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def set_categoria(self, categoria):
        self.__categoria = categoria
        
    def get_categoria(self):
        return self.__categoria
    
    def set_precio(self, precio):
        self.__precio = precio
        
    def get_precio(self):
        return self.__precio
  
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
        
    def get_cantidad(self):
        return self.__cantidad     