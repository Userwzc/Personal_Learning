# 二叉堆是一种能够动态排序的数据结构，是二叉树结构的延伸
# 主要操作就两个, sink(下沉) 和 swim(上浮),用以维护二叉堆的性质
# 二叉堆的主要应用有两个，首先是一种很有用的数据结构优先级队列(Priority Queue), 第二种是一种排序方法堆排序(Heap Sort)
# 能动态排序的常用数据结构其实只有两个，一个是优先级队列(底层用二叉堆实现),另一个是二叉搜索树。二叉搜索树的用途更广泛，优先级队列能做的事，二叉搜索树其实都能做。
# 但优先级队列的API和代码实现相较于二叉搜索树更简单，所以一般能用优先级队列解决的问题

# 性质：
# 1. 二叉堆中的每个节点都满足堆性质：对于最大堆，任意节点的值都大于等于其子节点的值；对于最小堆，任意节点的值都小于等于其子节点的值
# 2. 一个二叉堆的左右子堆(子树)也是一个二叉堆。

# 简化版优先队列实现：
# 增:push/swim方法插入元素
# 以小顶堆为例，向小顶堆中插入新元素遵循两个步骤：
# 1.先把新元素追加到二叉树底层的最右侧，保持完全二叉树的结构。此时该元素的父节点可能比它大，不满足小顶堆的性质
# 2.为了恢复小顶堆的性质，需要将这个元素不断上浮(swim)，直到它的父节点比它小为止，或者到达根节点。此时整个二叉树就满足小顶堆的性质了。

# 删：pop/sink方法删除元素
# 以小顶堆为例，删除小顶堆的堆顶元素遵循两个步骤：
# 1.先把堆顶元素删除，把二叉树底层的最右侧元素摘除并移动到堆顶，保持完全二叉树的结构。此时堆顶元素可能比它的子节点大，不满足小顶堆的性质。
# 2.为了恢复小顶堆的性质，需要将这个新的堆顶元素不断下沉(sink)，直到它比它的子节点小为止，或者到达叶子节点。此时整个二叉树就满足小顶堆的性质了。

# 查:peek方法查看堆顶元素
# 直接返回堆顶元素即可，不需要做任何调整。

# 由于push和pop操作都需要先找到二叉树最底层的最右侧节点，正常情况下需要O(log n)的时间复杂度，但通过使用数组来存储二叉堆，可以在O(1)时间内定位到该节点，从而使得push和pop操作的时间复杂度都为O(log n)。
# 使用数组来模拟二叉树，前提是二叉树是完全二叉树，这样才能保证节点在数组中的位置是连续的，没有空洞。
# 直接在数组的末尾追加元素，就相当于在完全二叉树的最后一层从左到右依次填充元素；数组中最后一个元素，就是完全二叉树的底层最右侧的元素，完美契合我们实现二叉堆的场景
# 在数组中，索引0空着不用，就可以根据任意节点的索引计算出父节点或左右节点的索引:
# def parent(node: int) -> int:
#     return node // 2

# def left(node: int) -> int:
#     return node * 2

# def right(node: int) -> int:
#     return node * 2 + 1 

# # 或者使用索引从0开始的方式:
# def parent(node: int) -> int:
#     return (node - 1) // 2

# def left(node: int) -> int:
#     return node * 2 + 1

# def right(node: int) -> int:
#     return node * 2 + 2 

class MyPriorityQueue:
    def __init__(self, capacity, comparator = None):
        self.heap = [0] * capacity
        self.size = 0
        self.comparator = comparator if comparator else lambda a, b: (a > b) - (a < b)  # 默认是小顶堆,升序
    
    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def parent(self, node):
        return (node - 1) // 2

    def left(self, node):
        return node * 2 + 1
    
    def right(self, node):
        return node * 2 + 2

    def swap(self, i ,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self.heap[0]

    def push(self, value):
        if self.size == len(self.heap):
            self.resize(2*len(self.heap))
        self.heap[self.size] = value
        self.swim(self.size)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        top = self.heap[0]
        self.swap(0, self.size - 1)
        self.heap[self.size - 1] = None
        self.size -= 1
        self.sink(0)

        if self.size > 0 and self.size == len(self.heap) // 4:
            self.resize(len(self.heap) // 2)
        return top

    # O(log n) 上浮
    def swim(self, index):
        while index > 0 and self.comparator(self.heap[index], self.heap[self.parent(index)]) < 0:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    # O(log n)  下沉
    def sink(self, index):
        while self.left(index) < self.size or self.right(index) < self.size:
            smallest = index
            if self.left(index) < self.size and self.comparator(self.heap[self.left(index)], self.heap[smallest]) < 0:
                smallest = self.left(index)
            if self.right(index) < self.size and self.comparator(self.heap[self.right(index)], self.heap[smallest]) < 0:
                smallest = self.right(index)
            if smallest == index:
                break
            self.swap(index, smallest)
            index = smallest
    
    def resize(self, capacity):
        assert capacity >= self.size
        new_heap = [0] * capacity
        for i in range(self.size):
            new_heap[i] = self.heap[i]
        self.heap = new_heap

if __name__ == "__main__":
    pq = MyPriorityQueue(3, comparator = lambda a, b : (a > b) - (a < b))  # 小顶堆
    pq.push(3)
    pq.push(1)
    pq.push(4)
    pq.push(1)
    pq.push(5)
    pq.push(9)
    while not pq.is_empty():
        print(pq.pop())
