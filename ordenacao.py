# Selection Sort

lista = [7, 5, 1, 8, 3]

def selection_sort(lista):
    for j in range(lista - 1):
        min_index = j
        for i in range(j, len(lista)):
            if lista[i] < lista[min_index]:
                min_index = i

        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux


# Bubble Sort