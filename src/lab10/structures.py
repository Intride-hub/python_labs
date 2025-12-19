from collections import deque
from typing import Any


class Stack:
    def __init__(self):
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Невозможно выполнить pop: стек пуст")
        return self._data.pop()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data})"


class Queue:
    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Невозможно выполнить dequeue: очередь пуста")
        return self._data.popleft()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"


# ================== DEMO ==================
if __name__ == "__main__":
    print("=== STACK DEMO ===")
    stack = Stack()
    print("Пустой стек:", stack)
    print("is_empty:", stack.is_empty())

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("После push:", stack)

    print("peek:", stack.peek())
    print("pop:", stack.pop())
    print("После pop:", stack)
    print("len:", len(stack))

    print("\n=== QUEUE DEMO ===")
    queue = Queue()
    print("Пустая очередь:", queue)
    print("is_empty:", queue.is_empty())

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print("После enqueue:", queue)

    print("peek:", queue.peek())
    print("dequeue:", queue.dequeue())
    print("После dequeue:", queue)
    print("len:", len(queue))
