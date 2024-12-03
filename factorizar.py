def recoger_numero():
    numero= input("dame un numero ")
    valor=int(numero)
    return valor
5

def factorizar_numero (x): 
    factores = []
    divisor = 2
    while x > 1:
        while x % divisor == 0:  # Verifica si 'divisor' es un factor de 'x'
            factores.append(divisor)
            x //= divisor  # Reduce 'x' dividiéndolo por 'divisor'
        divisor += 1  # Pasa al siguiente número para probar
    return factores

print("lista conlos factores de número")
print(factorizar_numero(recoger_numero()))