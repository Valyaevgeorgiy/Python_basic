# Сложность такого алгоритма в лучшем случае приблизительно равна O(n log(n))

from random import randint

lst_x = [randint(-100, 100) for _ in range(10)]
print('Исходный список:', str(lst_x) + '.', sep='\n')
print()

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

    return lst

print(f'Список после сортировки слиянием: \n{merge_sort(lst_x)}.')

# Исходный список:
# [-41, -99, 47, 19, -54, -59, -15, -84, 64, -67].
#
# Список после сортировки слиянием:
# [-99, -84, -67, -59, -54, -41, -15, 19, 47, 64].