# В таблице с прямой адресацией реализован принцип индексации массива:
# каждому элементу будет присвоен свой порядковый ключ из множества U = { 0, 1, ..., m - 1}, где m не слишком велико.

# Кроме того, предполагается, что никакие два элемента не имеют одинаковых ключей.
# Для представления динамического множества мы используем массив, или таблицу с прямой адресацией,
# каждая ячейка которого соответствует ключу из пространства ключей U.

# Возможность прямой индексации элементов обычного массива обеспечивает доступ к произвольной позиции
# в массиве за время O(1).

# Прямая индексация применима, если есть возможность выделить массив размера, достаточного для того,
# чтобы у каждого возможного значения ключа имелась своя ячейка.

def to_key(s=None):
    '''Возвращает ПОЛОЖИТЕЛЬНЫЙ ключ по символу.
    Если объект не задан, то возвращает максимальное значение ключа.'''
    if s is None:
        s = 'z'
    return ord(s) - ord('a') + 1


class DirectStrTable:
    def __init__(self, str_len):
        self._str_len = str_len  # максимальная длина строки в таблице
        self._n = self._to_key()  # количество допустимых символов
        self._none = object()  # создаем пустой объект в качестве внутреннего аналога None
        total = 0
        for i in range(self._str_len + 1):
            total *= self._n
            total += 1
        self._table = [self._none] * total
        self._len = 0  # текущее количество элементов, хранящихся в таблице

    # internal method
    def _to_key(self, s=None):

        '''Возвращает ПОЛОЖИТЕЛЬНЫЙ ключ по символу.
        Если объект не задан, то возвращает максимальное значение ключа.'''
        if s is None:
            s = 'z'
        return ord(s) - ord('a') + 1

    def _from_key(self, k):
        return chr(k + ord('a') - 1)

    # internal method
    def _str_to_key(self, seq):
        res = 0
        assert len(seq) <= self._str_len
        for i, el in enumerate(seq):
            assert 0 <= to_key(el) <= self._n  # проверка корректности рассматриваемого символа
            res += to_key(el) * self._n ** i
        return res

    def _key_to_str(self, k):
        s = ''
        while k > 0:
            k, m = divmod(k, self._n)
            if m == 0:
                s += self._from_key(self._n)
                k -= 1
            else:
                s += self._from_key(m)
            #             s += self._from_key(self._n) if m == 0 else self._from_key(m)
        return s

    # len(dst)
    def __len__(self):
        return self._len

    # dst[str_key]
    def __getitem__(self, str_key):
        k = self._str_to_key(str_key)
        if self._table[k] is self._none:
            raise KeyError(f'Key Error: {repr(s)}')  # по данному ключу значения в таблице нет
        else:
            return self._table[k]

    # str_key in dst
    def __contains__(self, str_key):
        k = self._str_to_key(str_key)
        if self._table[k] is self._none:
            return False
        else:
            return True

    # dst[str_key] = val
    def __setitem__(self, str_key, val):
        k = self._str_to_key(str_key)
        if self._table[k] is self._none:
            # в таблицу добавляется новый элемент
            self._table[k] = val
            self._len += 1
        else:
            # в таблице меняется значение существующего элемента
            self._table[k] = val

    # del dst[str_key]
    def __delitem__(self, str_key):
        k = self._str_to_key(str_key)
        if self._table[k] is self._none:
            raise KeyError(f'Key Error: {repr(s)}')  # по данному ключу значения в таблице нет
        else:
            self._table[k] = self._none
        self._len -= 1

    # for x in dst
    def _raw_iter(self):
        for rk, val in enumerate(self._table):
            if val is not self._none:
                yield rk, val  # self._key_to_str(rk)

    def __iter__(self):
        for rk, val in self._raw_iter():
            yield self._key_to_str(rk)  # , val #

    def items(self):
        for rk, val in self._raw_iter():
            yield self._key_to_str(rk), val

    def values(self):
        for val in self._table:
            if val is not self._none:
                yield val

    def stat(self):
        return f'Хранится элементов: {self._len}\nРазмер таблицы: {len(self._table)}\nДоля используемых элементов таблицы: {self._len / len(self._table)}'

dst = DirectStrTable(5)
dst['hello'] = 25
dst['z'] = 6
dst['zz'] = 8
dst['aaa'] = 9
dst['bye'] = 12

print('Таблица с прямой адресацией:')
print(list(dst._raw_iter()))
print()
print(dst.stat())