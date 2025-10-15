# 用双链表实现双端队列
from listnode import DoubleListNode

class MyListDeque:
    def __init__(self):
        self.list = DoubleListNode()

    def add_first(self, val):
        self.list.add_first(val)

    def add_last(self, val):
        self.list.add_last(val)

    def remove_first(self):
        return self.list.remove_first()

    def remove_last(self):
        return self.list.remove_last()

    def peek_first(self):
        return self.list.get(0)
    
    def peek_last(self):
        return self.list.get(self.list.size - 1)
    
if __name__ == "__main__":
    deque = MyListDeque()
    deque.add_last(1)
    deque.add_last(2)
    deque.add_last(3)
    print(deque.remove_first())  # 1
    print(deque.peek_first())    # 2
    print(deque.peek_last())     # 3
    deque.add_first(0)
    print(deque.peek_first())    # 0
    print(deque.remove_last())   # 3
    print(deque.peek_last())     # 2