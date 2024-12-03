class Coche:  # Declaración del constructor con parámetros
    def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):
        self.largo = largo
        self.ancho = ancho
        self.ruedas = ruedas
        self.peso = peso
        self.color = color
        self.is_enMarcha = is_enMarcha
        
    def __del__(self):
        print("Acabas de llamar al método destructor. El objeto acaba de sera eliminado")

    def __str__(self):
        return (f"Coche(largo={self.largo}, ancho={self.ancho}, ruedas={self.ruedas}, "
                f"peso={self.peso}, color={self.color}, is_enMarcha={self.is_enMarcha})")

# Declaración de dos instancias de clase pasándoles los parámetros requeridos en el constructor.
coche_1 = Coche(400, 160, 4, 1200, "amarillo", True)
coche_2 = Coche(420, 150, 4, 1500, "verde", False)


# Imprimir los objetos
print(coche_1)
print(coche_2)
del coche_2
