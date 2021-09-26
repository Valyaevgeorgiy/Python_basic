a, b, c, d = int(input()), int(input()), int(input()), int(input())
k = c
print(" ", end="\t")

while c != (d + 1):          # печатаем первую строку с изначальным табом)
    print(c, end="\t")
    c += 1
    if c == (d + 1):          # переходим на следующую строку
        print()

while a != (b + 1):          # заполняем оставшиеся столбцы таблицы умножения
    print(a, end="\t")
    for w in range(k, c):
        print(w * a, end="\t")
    print()
    a += 1