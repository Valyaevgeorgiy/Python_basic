# Сложность такого алгоритма в лучшем случае приблизительно равна O(n log(n))

from random import choice, randint

lst_x = [randint(-100, 100) for _ in range(10)]
print('Исходный список:', str(lst_x) + '.', sep='\n')
print()

def Fast_sort(lst):
    if len(lst) <= 1:
        return lst
    xls = choice(lst)
    ls1 = [i for i in lst if i < xls]
    lsx = [i for i in lst if i == xls]
    ls2 = [i for i in lst if i > xls]
    return Fast_sort(ls1) + lsx + Fast_sort(ls2)

print(f'Список после быстрой сортировки: \n{Fast_sort(lst_x)}.')

# Исходный список:
# [31, -38, -97, 38, 22, -28, 42, -1, -1, -67].
#
# Список после быстрой сортировки:
# [-97, -67, -38, -28, -1, -1, 22, 31, 38, 42].