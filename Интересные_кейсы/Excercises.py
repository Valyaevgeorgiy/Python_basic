def exercise1():
    count = 0
    s = ''
    x = 0
    xs = 0
    for a in range(1, 35):
        for b in range(1, 35):
            for c in range(1, 35):
                for d in range(1, 35):
                    if (a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d):
                        if ((a ** 3) + (b ** 3)) == ((c ** 3) + (d ** 3)):
                            count += 1
                            x = (a ** 3) + (b ** 3)
                            s += str(x) + ' '
                            if str(x) in s:
                                xs += 1
                                if xs == 1:
                                    print('x =', x)
                                    xs = 0
                                else:
                                    xs = 0
                            if count == 5:
                                break
            if count == 5:
                break
        if count == 5:
            break
    return 'Конец программы'

#exercise1()

def exercise2():
    age = 27
    txt = 'My name is Timur, I am {}'.format(age)
    print(txt)
    return 'Конец программы'

#exercise2()

def exercise3():
    from time import time
    start = time()
    a, flag = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88,
               -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91,
               44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24,
               -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38,
               -55, 7, -11, -26, -62, -84], 0

    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag += 1
        if flag == 0:
            break
    print(a)
    print(time() - start)

#exercise3()

def exercise4():
    a, a1 = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90,
             96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56,
             71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66,
             62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94,
             59], []
    cax = a[0]
    n = len(a)
    # реализация алгоритма сортировки выбором
    for i in range(n):
        cax = max(a)
        sd = a.index(cax)
        del a[sd]
        a1.append(cax)
    a1.reverse()
    print(a1)

#exercise4()

def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]

def exercise5():
    s = 'abcdabcaaa'
    char = 'a'
    print(find_all(s, char))

#exercise5()

def row_sum_odd_numbers(n):
    sx = 0
    if n == 1:
        print(1)
    else:
        ind2 = (n - 1) + (n * n)
        ind1 = ind2 - ((n - 1) * 2)
        for i in range(ind1, (ind2 + 1), 2):
            sx += i
        print(sx)

def exercise6():
    row_sum_odd_numbers(2)

#exercise6()

def convert_to_python_case(text):
    s = ''
    for i in range(len(text)):
        if i == 0:
            s += text[i].lower()
            continue
        if text[i].isupper():
            s += '_' + text[i].lower()
        else:
            s += text[i]
    return s

def exercise7():
    txt = 'ThisIsCamelCased'
    print(convert_to_python_case(txt))

#exercise7()

def exercise8():
    x, s, y = 15 // 2, '*', ''
    for i in range(8):
        y = ' ' * (x) + s
        y.strip()
        print(y)
        s += '**'
        x -= 1

#exercise8()

def exercise9(num):
    v1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    v2 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
    'восемнадцать', 'девятнадцать']
    v3 = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
    'девяносто']

    if num % 10 == 0:
        x = num // 10
        return v3[x - 1]
    elif num < 10:
        return v1[num - 1]
    elif 11 <= num <= 19:
        x = num % 10
        return v2[x - 1]
    elif 20 < num < 100:
        x1 = num // 10
        x2 = num % 10
        xx = v3[x1 - 1] + ' ' + v1[x2 - 1]
        return xx

#for i in range(1, 100):
    #print(exercise9(i))

def is_pangram(text):
    text1 = text.lower()
    alph = [chr(i) for i in range(97, 123)]
    for i in range(len(text)):
        if text1[i] == ' ':
            continue
        elif (text1[i] in alph):
            x = alph.index(text1[i])
            del alph[x]
    if len(alph) == 0:
        return True
    else:
        return False

def exercise10(text):
    print(is_pangram(text))

#exercise10('Jackdaws love my big sphinx of quartz')