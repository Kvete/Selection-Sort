from random import randint


def selection_sort(massiv):
    for j in range(len(massiv) - 1):
        min_index = j
        for i in range(j + 1, len(massiv)):
            if massiv[i] < massiv[min_index]:
                min_index = i
        temp = massiv[j]
        massiv[j] = massiv[min_index]
        massiv[min_index] = temp
    return massiv


array = []
for i in range(randint(2, 7)):
    array.append(randint(0, 99))

print(array)
print()
print(selection_sort(array))
