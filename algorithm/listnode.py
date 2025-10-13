# 带虚拟头尾的双链表
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
class DoubleListNode:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_last(self, val):
        node = Node(val)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def add_first(self, val):
        node = Node(val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def add(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        node = Node(val)
        node.prev = curr
        node.next = curr.next
        curr.next.prev = node
        curr.next = node
        self.size += 1

    def remove_first(self):
        if self.size == 0:
            raise IndexError("Remove from empty list")
        first = self.head.next
        self.head.next = first.next
        first.next.prev = self.head
        first.prev = None
        first.next = None
        self.size -= 1
        return first.val
    
    def remove_last(self):
        if self.size == 0:
            raise IndexError("Remove from empty list")
        last = self.tail.prev
        self.tail.prev = last.prev
        last.prev.next = self.tail
        last.prev = None
        last.next = None
        self.size -= 1
        return last.val
    
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        to_remove = curr.next
        curr.next = to_remove.next
        to_remove.next.prev = curr
        to_remove.prev = None
        to_remove.next = None
        self.size -= 1
        return to_remove.val
    
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index <= self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - index - 1):
                curr = curr.prev
        return curr.val
    
    def display(self):
        curr = self.head.next
        while curr != self.tail:
            print(f"{curr.val} <-> ", end="")
            curr = curr.next
        print("null\n")

list = DoubleListNode()
list.add_last(1)
list.add_last(2)
list.add_last(3)
list.add_first(0)
list.add(2, 100)
list.display()

#带虚拟头节点的单链表，尾节点指向末尾节点
class SNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleListNode:  
    def __init__(self):
        self.head = SNode(None)
        self.tail = self.head
        self.size = 0
        
    def add_last(self, val):
        node = SNode(val)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def add_first(self, val):
        node = SNode(val)
        node.next = self.head.next
        self.head.next = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def add(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        prev = self.head
        for _ in range(index):
            prev = prev.next
        node = SNode(val)
        node.next = prev.next
        prev.next = node
        if node.next is None:
            self.tail = node
        self.size += 1

    def remove_first(self):
        if self.size == 0:
            raise IndexError("Remove from empty list")
        first = self.head.next
        self.head.next = first.next
        if self.head.next is None:
            self.tail = self.head
        first.next = None
        self.size -= 1
        return first.val
    
    def remove_last(self):
        if self.size == 0:
            raise IndexError("Remove from empty list")
        prev = self.head
        while prev.next != self.tail:
            prev = prev.next
        last = self.tail
        prev.next = None
        self.tail = prev
        last.next = None
        self.size -= 1
        return last.val
    
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        prev = self.head
        for _ in range(index):
            prev = prev.next
        to_remove = prev.next
        prev.next = to_remove.next
        if to_remove == self.tail:
            self.tail = prev
        to_remove.next = None
        self.size -= 1
        return to_remove.val
    
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val
    
    def display(self):
        curr = self.head.next
        while curr:
            print(f"{curr.val} -> ", end="")
            curr = curr.next
        print("null\n")

slist = SingleListNode()
slist.add_first(1)
slist.add_first(2)
slist.add_last(3)
slist.add_last(4)
slist.add(2, 5)
print(slist.remove_first())
print(slist.remove_last())
print(slist.remove(1))
print(slist.get(0))
print(slist.get(slist.size - 1))
print(slist.get(1))
slist.display()
