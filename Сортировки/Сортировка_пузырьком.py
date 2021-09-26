# Сложность такого алгоритма в лучшем случае приблизительно равна O(n)

from random import randint

lst_x = [randint(-100, 100) for _ in range(10)]
print('Исходный список:', str(lst_x) + '.', sep='\n')
print()

def bubble_sort(lst):
    for i in range((len(lst) - 1), -1, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp
    return lst
print(f'Список после пузырьковой сортировки: \n{bubble_sort(lst_x)}.')

# Исходный список:
# [-8, 81, -55, 8, 94, -38, 68, 79, -92, -73].
#
# Список после пузырьковой сортировки:
# [-92, -73, -55, -38, -8, 8, 68, 79, 81, 94].