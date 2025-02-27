from nodo import Node

class Circular_List[K, V]:
    def _init_(self):
        self.size = 0
        self.head: Node[K, V] | None = None
        self.tail: Node[K, V] | None = None
        self.aux: Node[K, V] | None = None

    def _iter_(self):
        self.aux = self.head
        return self

    def _len_(self):
        return self.size

    def _next_(self):
        if self.aux is None:
            raise StopIteration
        node = self.aux
        if self.aux.next is self.head:
            self.aux = None
        else:
            self.aux = self.aux.next
        return node

    def append(self, key: K, value: V | None = None):
        new_node = Node(key, value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
        self.size += 1

    def prepend(self, key: K, value: V | None = None):
        new_node = Node(key, value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.tail.next = self.head
        self.size += 1

    def is_empty(self):
        return self.head is None and self.tail is None

    def find_at(self, index: int):
        current_index = 0
        current = self.head
        while current is not None:
            if current_index == index:
                return current
            else:
                if current is not self.tail:
                    current = current.next
                    current_index += 1
                else:
                    break
        raise ValueError("Elemento no encontrado")

    def find_by(self, key: K):
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            else:
                if current is self.tail:
                    break
                else:
                    current = current.next
        raise Exception("Elemento no encontrado")

    def shift(self):
        current = self.find_at(0)
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.size = 0
            print("\nNo hay elementos")
        else:
            self.head = self.head.next
            self.tail.next = self.head
            current.next = None
            self.size -= 1
        return current