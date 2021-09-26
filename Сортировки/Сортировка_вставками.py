# Сложность такого алгоритма в лучшем случае приблизительно равна O(n)

from random import randint

lst_x = [randint(-100, 100) for _ in range(10)]
print('Исходный список:', str(lst_x) + '.', sep='\n')
print()

def insertion_sort(lst):
    for inx in range(1, len(lst)):
        cunt_val = lst[inx]
        posn = inx
        while posn > 0 and lst[posn - 1] > cunt_val:
            lst[posn] = lst[posn - 1]
            posn -= 1
        lst[posn] = cunt_val
    return lst

print(f'Список после вставочной сортировки: \n{insertion_sort(lst_x)}.')

# Исходный список:
# [-17, -81, 10, -88, -5, -99, 50, -77, -11, 53].
#
# Список после вставочной сортировки:
# [-99, -88, -81, -77, -17, -11, -5, 10, 50, 53].
