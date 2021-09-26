print('----------8. Кортежи----------')

# Кортежи - не изменяемые списки.

t = (2,3,4) # создание кортежа
t1 = tuple()
t1 = tuple(i for i in range(10))
print(t1)
# Список тяжелее кортежа, кортеж работает быстрее
print()
a = tuple([i for i in range(10, 100, 10)])

# t[2] = 3 # выдаст ошибку, кортеж неизменяем, в отличие от списка


print('Tuple a :')
print(a)

from sys import getsizeof

a = tuple([i for i in range(1000)])
b = [i for i in range(1000)]

print('Различия во вместимости в ОЗУ данных с кортежа и списка :')
print(f'{getsizeof(a)} байт, {getsizeof(b)} байт')