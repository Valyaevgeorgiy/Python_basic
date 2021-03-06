print('----------7. Множества----------')
print()
# Множество - это неупорядоченная коллекция уникальных элементов, с которой можно сравнивать
# другие элементы, чтобы определить, принадлежат ли они этому множеству.

# Множество может содержать только элементы неизменяемых
# типов, например числа, строки, кортежи. Объявить множество можно с помощью конструктора set().

s = set([i for i in range(50, 150)])
s = set()  # создание множества
s0 = {2, 3, 4, 2}  # В множестве нет повторяющихся значений
print(s0)
s.add(10)  # добавление элемента
s.add(2)
s.add(50)
s.remove(2)  # вынос тела
s0.update(s)  # обновление
print(s0)

a = set([i for i in range(1, 101)])
b = set([i for i in range(50, 151)])

print('Set a:')
print(a)
print()
print('Set b:')
print(b)

print('Объединение множеств :')
print(a | b)

print('Пересечение множеств :')
print(a & b)

print('Разность множеств :')
print(a - b)

print('Ксор множеств :')
print(a ^ b)

a = {2, 4, 7, 9}

a.update({1, 3, 6, 8})

print('Set a :')
print(a)