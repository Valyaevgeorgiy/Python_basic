# Сложность такого алгоритма в лучшем случае приблизительно равна O(n)

from random import randint

lst_x = [randint(-100, 100) for _ in range(10)]
print('Исходный список:', str(lst_x) + '.', sep='\n')
print()


def step_insert_sort(lst, start, step):
    for i in range(start + step, len(lst), step):
        cur_value = lst[i]
        pos = i

        while pos >= step and lst[pos - step] > cur_value:
            lst[pos] = lst[pos - step]
            pos -= step

        lst[pos] = cur_value


def shell_sort(lst):
    sublst_c = len(lst) // 2

    while sublst_c > 0:
        for start_pos in range(sublst_c):
            step_insert_sort(lst, start_pos, sublst_c)

        sublst_c = len(lst) // 2

    return lst

print(f'Список после сортировки Шелла: \n{shell_sort(lst_x)}')

# Исходный список:
# [75, 58, 38, -44, -14, -99, 33, 4, -23, -38].
#
# Список после сортировки Шелла:
# [-99, -44, -38, -23, -14, 4, 33, 38, 58, 75]
