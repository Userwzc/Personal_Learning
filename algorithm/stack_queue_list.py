# 使用链表实现队列和栈
from collections import deque

class MyLinkedStack:
    def __init__(self):
        self.list = deque()
    
    def push(self, val):
        self.list.append(val)

    def pop(self):
        return self.list.pop()
    
    def peek(self):
        return self.list[-1]
    
    def size(self):
        return len(self.list)
    

class MyLinkedQueue:
    def __init__(self):
        self.list = deque()
    
    def enqueue(self, val):
        self.list.append(val)

    def dequeue(self):
        return self.list.popleft()

    def peek(self):
        return self.list[0]

    def size(self):
        return len(self.list)

if __name__ == "__main__":
    stack = MyLinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    queue = MyLinkedQueue()
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