"""     Ejercicio Final Luciano.ga.al@gmail.com
        Programa Gestion de Stock  (permite 6 opciones por teclado)
        1 Agregar producto                 
        2 Modificar precio a un producto   
        3 Eliminar producto                     
        4 Buscar producto                     
        5 Resumen inventario
        0 Salir Gestion de Stock                 
    Contiene 2 clases (Producto e Inventario) y la funcion ingresar_nombre()
"""

from Inventario import Inventario

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
                supermercado.modificar_precio(nombre_m)  #si existe el nombre del producto podemos modificar precio
        elif escoger == 3:
            nombre_m = ingresar_nombre()
            si_esta = supermercado.buscar_producto(nombre_m)  
            if si_esta == True:                             #si existe el nombre del producto podemos eliminar el producto
                supermercado.eliminar_producto(nombre_m)
        elif escoger == 4:
            nombre_m = ingresar_nombre()
            si_esta = supermercado.buscar_producto(nombre_m)
            if si_esta == True:                             #si existe el nombre del producto listamos los atributos              
                supermercado.buscar_producto_nombre(nombre_m)
        elif escoger == 5:
            supermercado.listar_inventario()                    
        elif escoger == 0:
            print("Salió de Gestion de Stock")
            break
        else:
            print("Opción inválida, pulsa un número entre 0 y 5") #si no es ninguna opcion entre 0 y 5 vuelve a preguntar


