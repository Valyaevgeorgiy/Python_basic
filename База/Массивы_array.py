# Динамический массив - это тип данных, который по сути представляет собой нечто среднее
# между встроенным типом 'list' и типом numpy 'ndarray'.

# Разница между ними заключается в том, что размер динамического массива может быть
# динамически изменен во время выполнения. Нам не нужно заранее указывать размер массива.

# В динамическом массиве, как только заразная память заполнена, выделяется больший кусок памяти.
# Содержимое исходного массива копируется в это новое пространство, и доступные слоты заполняются непрерывно.

# Как и ndarray, элементы в массивах являются типами C, указанными при инициализации.
# Они не являются указателями на объекты Python;

# Это может помочь избежать некоторых неправильных и семантических ошибок и немного повысить производительность.
from array import array

x = array('d')          #'d' denotes an array of type double
x.append(1.1)
x.append(2.2)
print(x)
print()
print(x.pop())
print()
print(x)


import ctypes
from random import randint


class DArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.amount = 0
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return f'Length of array list: {self.amount}.'

    def __getitem__(self, item):
        if 0 <= item <= self.amount:
            return self.array[item]
        else:
            return f'Указанный индекс выходит за границы массива'

    def __str__(self):
        output_list = []
        for i in range(self.amount):
            output_list.append(self.array[i])
        return f'Array list: {output_list}'

    def append(self, element):
        if self.amount == self.capacity:
            new_capacity = 2 * self.capacity
            new_array = self.make_array(new_capacity)
            for i in range(self.amount):
                new_array[i] = self.array[i]
            self.capacity = new_capacity
            self.array = new_array
        self.array[self.amount] = element
        self.amount += 1

    def newitem(self, index, element):
        if 0 <= index <= self.amount:
            self.array[index] = element
            print(f"Element {element} - it's a new element of array list")
        else:
            return f'Указанный индекс выходит за границы массива'

    def delitem(self):
        if self.amount == 0:
            print("Array list is empty")
        else:
            if self.amount <= self.capacity:
                flag, rez = False, randint(0, self.amount - 1)
                new_array = self.make_array(self.capacity)
                for i in range(self.amount):
                    if (rez == i) and (i == self.amount - 1):
                        break
                    else:
                        if i == rez:
                            new_array[i] = self.array[i + 1]
                            flag = True
                            continue
                        elif flag:
                            if i != self.amount - 1:
                                new_array[i] = self.array[i + 1]
                            else:
                                break
                        else:
                            new_array[i] = self.array[i]
                self.array = new_array
                self.amount -= 1
                print(f"Index {rez} was deleted.")

    def make_array(self, length):
        return (length * ctypes.py_object)()

ar = DArray(6)

ar.append(12)
ar.append(41)
ar.append(10)
ar.append(79)
ar.append(4)

print(ar)
print()

print(ar.__len__())

print("Max capacity array list:", ar.capacity)

ar.newitem(3, 100000)

print(ar)

ar.delitem()

print(ar)