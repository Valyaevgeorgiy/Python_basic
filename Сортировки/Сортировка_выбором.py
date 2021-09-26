# Сложность алгоритма в лучшем случае приблизительно равна O(n ^ 2)

from random import randint

lst_x = [randint(-100, 100) for _ in range(10)]
print('Исходный список:', str(lst_x) + '.', sep='\n')
print()

def selection_sort(lst):
    for fl_st in range(len(lst) - 1, -1, -1):
        ps_max = 0
        for n in range(1, fl_st + 1):
            if lst[n] > lst[ps_max]:
                ps_max = n
        tmp = lst[fl_st]
        lst[fl_st] = lst[ps_max]
        lst[ps_max] = tmp
    return lst

print(f'Список после выборочной сортировки: \n{selection_sort(lst_x)}.')

# Исходный список:
# [-30, -17, 56, 82, 89, 79, 4, 57, -96, 17].
#
# Список после выборочной сортировки:
# [-96, -30, -17, 4, 17, 56, 57, 79, 82, 89].
