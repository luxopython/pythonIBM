import random
aleatorio = random.randint(1,100)
print (aleatorio)

def recoger_numero():
    numero= input("dame un numero ")
    valor=int(numero)
    return valor
    
for i in range(3):
    print(recoger_numero())
    
    
    
def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print(x) # Llamamos a f2 desde f1

    f2(b)
    
f1(aleatorio) # Llamamos a f1

def maxmin(lista):
    return max(lista), min(lista) # Devielveuna tupla de 2 elementos

l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(l) # Desempaqueta la tupla en 2 variables
print(minimo, maximo)

