# 使用数组实现队列和栈
class MyArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
from circle_arr import CycleArray

class MyArrayQueue:
    def __init__(self):
        self.queue = CycleArray()

    def enqueue(self, val):
        self.queue.add_last(val)

    def dequeue(self):
        return self.queue.remove_first()

    def size(self):
        return self.queue.count

    def peek(self):
        return self.queue.get_first()
    
if __name__ == "__main__":
    stack = MyArrayStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    queue = MyArrayQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(stack.pop())  # 3
    print(stack.peek()) # 2
    print(stack.size()) # 2
    print("*"*30)
    print(queue.dequeue())  # 1
    print(queue.peek())     # 2
    print(queue.size())     # 2