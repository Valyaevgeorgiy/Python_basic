# Односвязный список - это специфичный список, в котором элементы связаны друг с другом узлами (связями),
# и при этом имеется голова - направленность списка из начала в конец (единственная).

class Linfed_List:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element

        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

        return element

    def insert(self, element, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = self.Node(element, next_node=node)

        return element

    def asign(self, element, index):
        node = self.head
        i = 0

        while i < index:
            node = node.next_node
            i += 1

        node.element = element

    def get(self, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        return node.element

    def out(self):
        node = self.head
        print('[', end='')

        while node.next_node:
            print(node.element, end=', ')
            node = node.next_node
        print(node.element, end=']')

    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node

        node = self.head
        prev_node = node
        i = 0

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        element = node.element

        del node

        return element

    def get_length(self):
        if not self.head:
            return 0

        i = 1
        node = self.head

        while node.next_node:
            i += 1
            node = node.next_node

        return i

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

linked_list = Linfed_List()

linked_list.append(12)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(67)
linked_list.insert(15, 1)

print("Second element is:", linked_list.get(1))
print()
print('Your Linked List:')
linked_list.out()

print()

print('Deleted element:', linked_list.delete(4))
linked_list.out()

print()
print('Length Linked List:', linked_list.get_length())

linked_list.asign(450, 3)
print("Your Linked List now:")
linked_list.out()
print()
print(f'Your Linked List is empty? ... {linked_list.is_empty()}, of course.')