from nodo import Node

class List[T]:
    def _init_(self):
        self.size = 0
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def append(self, value: T):
        new_node = Node[T](value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def preprend(self, value: T):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1

        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    # Remover al inicio
    def shift(self):
        if self.head is None:  # Si la lista está vacía
            raise Exception("Lista Vacía")

        elif self.head is self.tail:  # Si solo hay un nodo en la lista
            aux = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return aux.value

        else:  # Si hay más de un nodo
            aux = self.head
            self.head = self.head.next
            self.size -= 1
            return aux.value

    #Remover al final
    def pop(self):
        if self.head is None and self.tail is None:
            raise Exception("Lista Vacía")

        elif self.head is self.tail:
            aux = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return aux.value

        else:
            prev: Node | None = None
            aux: Node | None = self.head
            while aux is not None:
                prev = aux
                aux = aux.next
                if aux is self.tail:
                    break
            self.tail = prev
            self.tail.next = None
            self.size -= 1
            return aux.value

    def show(self):
        aux = self.head
        while aux is not None:
            print(aux.value)
            aux = aux.next