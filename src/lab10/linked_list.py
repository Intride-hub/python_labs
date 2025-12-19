from typing import Any, Iterator


class Node:
    def __init__(self, value: Any, next: "Node | None" = None):
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value, self.head)
        self.head = new_node

        if self._size == 0:
            self.tail = new_node

        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("Индекс вне диапазона")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError("Индекс вне диапазона")

        if idx == 0:
            self.head = self.head.next
            if self._size == 1:
                self.tail = None
            self._size -= 1
            return

        prev = self.head
        for _ in range(idx - 1):
            prev = prev.next

        if prev.next == self.tail:
            self.tail = prev

        prev.next = prev.next.next
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(map(str, self))}])"

    def pretty(self) -> str:
        parts = []
        current = self.head
        while current:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)


# ================== DEMO ==================
if __name__ == "__main__":
    print("=== SINGLY LINKED LIST DEMO ===")

    lst = SinglyLinkedList()
    print("Пустой список:", lst)
    print("len:", len(lst))

    lst.append(1)
    lst.append(2)
    lst.append(3)
    print("После append:", lst)
    print("pretty:", lst.pretty())

    lst.prepend(0)
    print("После prepend:", lst)
    print("pretty:", lst.pretty())

    lst.insert(2, 99)
    print("После insert(2, 99):", lst)
    print("pretty:", lst.pretty())

    lst.remove_at(2)
    print("После remove_at(2):", lst)
    print("pretty:", lst.pretty())

    print("Итерация по списку:")
    for value in lst:
        print(value)

    print("len:", len(lst))
