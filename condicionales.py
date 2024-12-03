# Programa que pide una nota por consola y valora si el alumno ha aprobado o no.

notaIn=int(input("Introduzca nota:"))
if notaIn<5:
        calificacion="Suspenso"
else: calificacion="Aprobado"
print(calificacion)

# IF no sólo evalúa un boleano, también si una variable contiene información
variable = 19
if variable:
    print("Contiene información")
else:
    print("No contiene información")

#En este ejemplo sí evalúa un boleano
variable = 19
if variable == True:
    print("Contiene información")
else:
    print("No contiene información")
    
# Programa que pide una edad por consola y valora si el usuario es mayor de edad o no.
edad=int(input("Introduce edad: "))
if edad<18:
    print("No puedes pasar")
elif edad>100:
    print("Edad incorrecta")
else:
    print("Adelante")