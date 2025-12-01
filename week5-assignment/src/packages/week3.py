"""
week3.py
Simple data structures (Stack, Queue, LinkedList) and a small CSV loader/saver.
This file is intended for learning and demonstration.
"""

from typing import Any, Iterable, Optional, List
import csv
import io


# ---- Stack ----
class Stack:
    def __init__(self):
        self._data: List[Any] = []

    def push(self, x: Any) -> None:
        self._data.append(x)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


# ---- Queue (simple FIFO) ----
class Queue:
    def __init__(self):
        self._data: List[Any] = []

    def enqueue(self, x: Any) -> None:
        self._data.append(x)

    def dequeue(self) -> Any:
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.pop(0)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


# ---- Singly Linked List (minimal) ----
class Node:
    def __init__(self, val: Any):
        self.val = val
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self, items: Optional[Iterable[Any]] = None):
        self.head: Optional[Node] = None
        if items:
            for it in items:
                self.append(it)

    def append(self, val: Any) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self) -> List[Any]:
        out = []
        cur = self.head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out


# ---- CSV helpers ----
def read_csv_string(csv_text: str) -> List[dict]:
    """
    Parse CSV text into list of dicts. Useful for small test data.
    """
    f = io.StringIO(csv_text)
    reader = csv.DictReader(f)
    return list(reader)


def write_csv_string(rows: List[dict], fieldnames: List[str]) -> str:
    f = io.StringIO()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for r in rows:
        writer.writerow(r)
    return f.getvalue()


# ---- Demo ----
def quick_demo():
    s = Stack()
    s.push(1)
    s.push(2)
    print("Stack pop:", s.pop())

    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    print("Queue dequeue:", q.dequeue())

    ll = LinkedList([1, 2, 3])
    print("LinkedList ->", ll.to_list())

    csv_text = "name,age\nAlice,30\nBob,25\n"
    rows = read_csv_string(csv_text)
    print("CSV rows:", rows)
    print("CSV reserialised:\n", write_csv_string(rows, ["name", "age"]))


if __name__ == "__main__":
    quick_demo()

