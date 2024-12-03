# Declaración de la clase
class Coche():
# Declaración de atributos
    largo = 250
    ancho = 120
    ruedas = 4
    peso = 900
    color = "rojo"
    is_enMarcha = False
# Declaración de métodos
    def arrancar(self): # self hace referencia a la instancia de clase.
        self.is_enMarcha = True # Es como si pusiésemos miCoche.is_enMarcha = True
        
    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche esta arrancado"
        else:
            return "El coche está parado"
        

miCoche = Coche()
miCoche2 = Coche()

# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
print("El largo del coche es de" , miCoche.largo, "cm.")
miCoche.arrancar()
print(miCoche.estado())

# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("como esta el coche?:" , miCoche.estado())
miCoche.is_enMarcha = False
print("vamos a parar el coche:" , miCoche.estado())

# Modificamos el valor de una propiedad
print(miCoche.ruedas)
miCoche2.ruedas = 10
print("El coche2 tiene:" , miCoche2.ruedas, "ruedas.")