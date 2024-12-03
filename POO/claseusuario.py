# CREACIÓN DE LA CLASE
class Usuario:
    # Declaración de atributos
    nombre = "Angel"
    edad = 47
    login = "admin"
    password = "1234"
    email = "angel@loquesea.com"
    telefono = 666666666

    # Declaración de métodos
    def resumen(self):  # self hace referencia a la instancia de clase.
        print(f'Los datos del usuario son:\n'
              f'Nombre: {self.nombre}\n'
              f'Edad: {self.edad}\n'
              f'Login: {self.login}\n'
              f'Password: {self.password}\n'
              f'Email: {self.email}\n'
              f'Teléfono: {self.telefono}')

    def cambiaEdad(self):
        edadIntroducida = int(input("Introduce edad entre 18-100: "))
        if 18 < edadIntroducida < 100:
            self.edad = edadIntroducida
            print("Edad introducida correcta")
        else:
            print("La edad introducida no es correcta.")
            self.cambiaEdad()

    def muestraEdad(self):
        print('La edad del usuario es:', self.edad, 'años.')

# Creación de una instancia de la clase Usuario a la que llamaremos administrador
administrador = Usuario()

# Una vez creado el objeto administrador, hacemos uso del método “resumen()” perteneciente a la clase Usuario
administrador.resumen()
administrador.cambiaEdad()
administrador.muestraEdad()

