# Creo una estructura para los clientes
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)  # Aquí corregimos la indentación

# Y otra para las empresas
class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        encontrado = False
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                encontrado = True
                break  # Salir del bucle si el cliente es encontrado
        if not encontrado:
            print("Cliente no encontrado")  # Ahora usamos print, no return

    def borrar_cliente(self, dni=None):
        encontrado = False
        for i, c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c), "> BORRADO")
                encontrado = True
                break  # Salir del bucle después de borrar
        if not encontrado:
            print("Cliente no encontrado")  # Ahora usamos print, no return

    def __str__(self):
        # Devuelve la representación de todos los clientes
        return "\n".join(str(cliente) for cliente in self.clientes)

# Ahora utilizaré ambas estructuras
# Creo un par de clientes
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")

# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])

# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa)  # Aquí se usa __str__ de la clase Empresa

print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")

print("\n==BORRAR CLIENTES POR DNI==")
# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa)  # Aquí se usa __str__ de la clase Empresa
