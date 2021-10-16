d91 = dict(zip('abcd', range(4)))
print()
print(d91)
print()

d91['a'] = d91['a'] + 1
print(d91)
print()

d91['a'] = d91.get('a', 0) + 1
print(d91)
print()

d91['e'] = d91.get('e', 0) + 1
print(d91)
print()

print('Метод get()')
print(d91.get('www'))
print(d91)
print()

print('Метод setdefault()')
print(d91.setdefault('www'))
print(d91)
print()

d14 = dict(a=5, b=12, c=9, d=5)
print(d14)
print()
print('Метод pop()')
f = d14.pop('a')
print(f)
print(d14)
print()