from nodo import Node

class List:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def shift(self):
        if self.head is None:
            raise Exception("Lista Vacía")
        elif self.head is self.tail:
            aux = self.head
            self.head = None
            self.tail = None
        else:
            aux = self.head
            self.head = self.head.next
        self.size -= 1
        return aux.value

    def pop(self):
        if self.head is None and self.tail is None:
            raise Exception("Lista Vacía")
        elif self.head is self.tail:
            aux = self.head
            self.head = None
            self.tail = None
        else:
            prev = None
            aux = self.head
            while aux.next is not None:
                prev = aux
                aux = aux.next
            self.tail = prev
            self.tail.next = None
        self.size -= 1
        return aux.value

    def show(self):
        aux = self.head
        while aux is not None:
            print(aux.value)
            aux = aux.next