# Definição da função de ordenação bubble sort
from ast import Return


def bubble_sort(v):
    # Número de elementos na lista
    n = len(v)

    # Laço para percorrer a lista
    for i in range(n - 1):
        # Laço interno para comparação e troca
        for j in range(n - i - 1):
            # Comparar elementos adjacentes
            if v[j] > v[j + 1]:
                # Se o elemento da esquerda for maior, troque-os
                v[j], v[j + 1] = v[j + 1], v[j]

                # Mostrar a lista após cada troca
                print(f"Troca: {v}")


# Lista a ser ordenada
v = [12, 14, 65, 78, 23, 45, 18, 34, 75, 93]

# Ordenação usando bubble sort
bubble_sort(v)

# Lista ordenada final
print("Lista ordenada:", v)


def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]

        j = i - 1

        while j >= 0 and x < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = x


def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio + 1, fim)
        intercala(v, ini, meio, fim)


def intercala(v, ini, meio, fim):
    L = v[ini : meio + 1]
    R = v[meio + 1 : fim + 1]
    L.append(999)  # sentinela
    R.append(999)  # sentinela
    i = 0
    j = 0
    for k in range(ini, fim + 1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1
