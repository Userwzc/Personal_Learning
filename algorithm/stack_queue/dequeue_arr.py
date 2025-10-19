# 用数组实现双端队列

from algorithm.arr.circle_arr import CycleArray

class MyArrayDeque:
    def __init__(self):
        self.deque = CycleArray()

    def add_first(self, val):
        self.deque.add_first(val)

    def add_last(self, val):
        self.deque.add_last(val)

    def remove_first(self):
        return self.deque.remove_first()

    def remove_last(self):
        return self.deque.remove_last()

    def size(self):
        return self.deque.count

    def peek_first(self):
        return self.deque.get_first()
    
    def peek_last(self):
        return self.deque.get_last()
    
if __name__ == "__main__":
    deque = MyArrayDeque()
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