print('----------3. Циклы----------')
print()

for _ in range(10, 3, -3): # шаг -3
    print(_)

print()

for k, j in enumerate([i for i in range(0, 110, 20)]):
    print(f'({k}, {j})')

print()

a = 100
while a > 0:
    print(a, end="\n\t")
    a -= 1
