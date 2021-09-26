print('----------9. Генераторы----------')
print()
print((i for i in range(100)), ' -> ')
print('->', 'это объект-генератор, в котором просто есть range(100)')

print('Тернарный оператор с условиями :')
c = 1 if type('privet') == str else 500
print('Итоговый ответ тут равен', c)

print('Выражение посложнее :')
b = (i if i > 30 else 1 / i for i in range(50) if i % 5 in [1, 4])

for i in b:
    print(i)

print('Генератор словарей :')
a = {i: i * 20 for i in range(10)}
print(a)

gen = [ъ for ъ in range(11)]
print(gen)
gen1 = [i for i in range(11) if i%3 == 0]
print('Элементы, кратные 3:', gen1)
gen1 = [1 if i%3 == 0 else 0 for i in range(11)] # 1 - если кратен трем, 0 - если не кратен
print(gen1)
gen2 = {i:i*'Сынба' for i in range(1,11)} # генератор словаря
print(gen2)