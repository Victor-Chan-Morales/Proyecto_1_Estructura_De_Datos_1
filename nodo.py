class Node[K, V]:
    def __init__(self, key: K, value: V | None = None):
        self.key: K = key
        self.value: V | None = value
        self.next: Node | None = None