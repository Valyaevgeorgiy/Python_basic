def challen1():
    import matplotlib.pyplot as plt
    from random import randint
    arr = [randint(1, 20) for _ in range(50)]
    x = [i for i in range(50)]
    fig = plt.figure()     # создаём фигуру

    #plt.scatter(1, 1)
    #plt.show()
    plt.scatter(x, arr)     # отмечаем маркером точки на фигуре
    plt.show()

# challen1()
# это построение графика, состоящего из одной точки либо графика из рандомных точек

def challen2():
    import matplotlib.pyplot as plt
    x = [i for i in range(-10, 11)]
    y = [i*i for i in range(-10, 11)]

    fig, ax = plt.subplots()
    ax.set_title('График параболы')
    ax.set_xlabel('ось абсцисс')
    ax.set_ylabel('ось ординат')
    ax.scatter(x, y)
    plt.show()

challen2()
# построение параболы по точкам
