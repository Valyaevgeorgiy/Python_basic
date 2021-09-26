# По факту, стек - это разновидность динамического массива, в котором элементы связаны индексацией друг с другом.

class Stack:
    def __init__(self, a):
        self._maxlen = a
        self._stacc = []

    def __len__(self):
        return len(self._stacc)

    def push(self, e):
        if self._maxlen > len(self._stacc):
            self._stacc.append(e)
        else:
            raise IndexError("Stack's len is already max!")

    def poop(self):
        if not len(self._stacc) == 0:
            e = self._stacc[-1]
            self._stacc.pop()
        else:
            raise IndexError("Stack is empty")
        return e

    def toop(self):
        if not len(self._stacc) == 0:
            e = self._stacc[-1]
        else:
            raise IndexError("Stack is empty")
        return e

    def is_empty(self):
        if len(self._stacc) == 0:
            return True
        else:
            return False

    def __str__(self):
        return f"Final list is {self._stacc}"

s1 = Stack(3)

s1.push(42)
s1.push(23)
s1.push(150)

print(s1)
print()
print("Len of stack:", len(s1))
print("Top method:", s1.toop())
print("Pop method:", s1.poop())
print("Top method rightnow:", s1.toop())
print("This stack is empty? ...", s1.is_empty())