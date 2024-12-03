keys = ['nombre', 'apellidos', 'edad', 4]
values = ['Guido', 'van Rossum', '60', 6]

d = dict(zip(keys, values)) # Creamos el diccionario
d['Calle'] ='cobalto'   #se pueden añadir valores manualmente
for k in d:
    info = '{}: {}'.format(k, d[k]) 
# Texto formateado con claves y valores
    print(info)
    
'''El método str.format sustituye las llaves
de la cadena de texto por los parámetros
que le pasamos al llamarlo. En cada
iteración del ejemplo le estamos pasando
la clave (k) del diccionario y el valor del
diccionario correspondiente a esa clave
(d[k]).'''