st1 = 0
xs = 0
xsval = []
xscount = []
lst = list()
while st1 != 'end':
    st1 = input()
    if st1 != 'end':
        st2 = st1.split()
        xscount.append(len(st2))
        for i in range(len(st2)):
            st2[i] = int(st2[i])
        lst.append(st2)
    else:
        break
print(lst)

if sum(xscount) == len(lst):
    for i in range(len(lst)):
        if i != (len(lst) - 1):
            xs += lst[i][0] + lst[i][0] + lst[i - 1][0] + lst[i + 1][0]
            xsval.append(xs)
            xs = 0
        else:
            xs += lst[i][0] + lst[i][0] + lst[i - 1][0] + lst[0][0]
            xsval.append(xs)
            xs = 0
    print(xsval)
    count = 0
    coss = ''
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = str(xsval[count])
            count += 1
    for i in range(len(lst)):
        print(' '.join(lst[i]))

else:
    lst1 = list()
    lst0 = list()
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j == 0:
                if i != (len(lst) - 1):
                    xs += lst[i][j + 1] + lst[i + 1][j] + lst[i - 1][j] + lst[i][j - 1]  # справа - снизу - сверху - слева
                    xsval.append(xs)
                    xs = 0
                else:
                    xs += lst[i][j + 1] + lst[0][j] + lst[i - 1][j] + lst[i][j - 1]      # справа - снизу - сверху - слева
                    xsval.append(xs)
                    xs = 0
            elif j == (len(lst[i]) - 1):
                if i != (len(lst) - 1):
                    xs += lst[i][0] + lst[i - 1][j] + lst[i][j - 1] + lst[i + 1][j]      # справа - сверху - слева - снизу
                    xsval.append(xs)
                    xs = 0
                else:
                    xs += lst[i][0] + lst[i][j - 1] + lst[i - 1][j] + lst[0][j]          # справа - слева - сверху - снизу
                    xsval.append(xs)
                    xs = 0
            elif (i == 0) and (j != 0) and (j != (len(lst[i]) - 1)):
                if i != (len(lst) - 1):
                    xs += lst[i][j - 1] + lst[i][j + 1] + lst[i + 1][j] + lst[i - 1][j]      # слева - справа - снизу - сверху
                    xsval.append(xs)
                    xs = 0
                else:
                    xs += lst[i][j - 1] + lst[i][j + 1] + lst[0][j] + lst[i - 1][j]
                    xsval.append(xs)
                    xs = 0
            elif (i == (len(lst) - 1)) and (j != 0) and (j != (len(lst) - 1)):
                xs += lst[i][j - 1] + lst[i][j + 1] + lst[0][j] + lst[i - 1][j]          # слева - справа - снизу - сверху
                xsval.append(xs)
                xs = 0
            else:
                if i != (len(lst) - 1):
                    xs += lst[i - 1][j] + lst[i + 1][j] + lst[i][j - 1] + lst[i][j + 1]      # сверху - снизу - слева - справа
                    xsval.append(xs)
                    xs = 0
                else:
                    xs += lst[i - 1][j] + lst[0][j] + lst[i][j - 1] + lst[i][j + 1]
                    xsval.append(xs)
                    xs = 0
    print(xsval)
    count = 0
    coss = ''
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = str(xsval[count])
            count += 1
    for i in range(len(lst)):
        print(' '.join(lst[i]))