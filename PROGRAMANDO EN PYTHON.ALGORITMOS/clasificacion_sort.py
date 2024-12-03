#Insertion Sort
def insertion_sort(arr, n): #le pasamos la lista (arr) y la longitud (n) de la lista a la funcion
    for i in range(1, n):
        # posición actual y elemento
        current_position = i
        current_element = arr[i]

        # iterar hasta llegar al primer elemento o cuando el elemento actual sea menor que el anterior
        while current_position > 0 and current_element < arr[current_position - 1]:
            # actualizar el elemento actual con el elemento anterior
            arr[current_position] = arr[current_position - 1]
            # moverse a la posición anterior
            current_position -= 1
        
        # actualizar el elemento en la posición actual
        arr[current_position] = current_element

# inicialización del array
arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
insertion_sort(arr, len(arr))
print("Array ordenado:", arr)

#Selection sort
def selection_sort(arr, n):
    for i in range(n):
        # Para almacenar el índice del elemento mínimo
        min_element_index = i
        for j in range(i + 1, n):
            # Comprobando y actualizando el índice del elemento mínimo
            if arr[j] < arr[min_element_index]:
                min_element_index = j
        
        # Intercambiando el elemento actual con el elemento mínimo encontrado
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]

# Inicialización del array
arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
selection_sort(arr, len(arr))
print("Array ordenado:", arr)


#Bubble sort
def bubble_sort(arr, n):
    for i in range(n):
        # Iterando de 0 a n-i-1 ya que los últimos i elementos ya están ordenados
        for j in range(n - i - 1):
            # Comprobando el siguiente elemento
            if arr[j] > arr[j + 1]:
                # Intercambiando los elementos adyacentes
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Inicialización del array
arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
bubble_sort(arr, len(arr))
print("Array ordenado:", arr)


#merge sort
def merge(arr, left_index, mid_index, right_index):
    # Matrices izquierda y derecha
    left_array = arr[left_index:mid_index+1]
    right_array = arr[mid_index+1:right_index+1]

    # Longitudes de matriz izquierda y derecha
    left_array_length = mid_index - left_index + 1
    right_array_length = right_index - mid_index

    # Índices para fusionar las dos matrices
    i = j = 0
    # Índice para el reemplazo de elementos en la matriz original
    k = left_index

    # Iterando sobre las dos submatrices y fusionándolas
    while i < left_array_length and j < right_array_length:
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    # Agregando elementos restantes de la matriz izquierda, si hay
    while i < left_array_length:
        arr[k] = left_array[i]
        i += 1
        k += 1

    # Agregando elementos restantes de la matriz derecha, si hay
    while j < right_array_length:
        arr[k] = right_array[j]
        j += 1
        k += 1

def merge_sort(arr, left_index, right_index):
    # Caso base para la función recursiva
    if left_index >= right_index:
        return
    
    # Encontrar el índice medio
    mid_index = (left_index + right_index) // 2
    
    # Llamadas recursivas para dividir la matriz
    merge_sort(arr, left_index, mid_index)
    merge_sort(arr, mid_index + 1, right_index)
    
    # Fusionando las dos sub-matrices
    merge(arr, left_index, mid_index, right_index)

# Inicialización de la matriz
arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
merge_sort(arr, 0, len(arr) - 1)
print("Array ordenado:", arr)
