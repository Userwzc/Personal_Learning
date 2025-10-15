# 环形数组  O(1) 时间复杂度实现数组头部增删元素
# 利用mod运算实现环形数组
# eg
# arr = [1,2,3,4,5]
# i = 0
# while i < len(arr):
#    print(arr[i])
#    i = (i + 1) % len(arr)  # 环形访问

class CycleArray:
    def __init__(self, size = 1):
        self.size = size
        self.arr = [None] * size
        self.start = 0  # start 指向第一个元素
        self.end = 0    # end 指向最后一个元素的下一个位置
        self.count = 0 # 当前元素个数

    
    def resize(self, newSize):
        new_arr = [None] * newSize
        for i in range(self.count):
            new_arr[i] = self.arr[(self.start + i) % self.size]
        self.arr = new_arr
        # 重置 start 和 end
        self.start = 0
        self.end = self.count
        self.size = newSize
    
    # O(1)
    def add_first(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        # 闭区间，先左移，再赋值
        self.start = (self.start - 1 + self.size ) % self.size
        self.arr[self.start] = val
        self.count += 1

    # O(1)
    def add_last(self,val):
        if self.is_full():
            self.resize(self.size * 2)
        # 开区间，先赋值，再右移
        self.arr[self.end] = val
        self.end = (self.end + 1) % self.size
        self.count += 1 

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Remove from empty array")
        val = self.arr[self.start]
        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1
        if self.count > 0 and self.count == self.size // 4:
            self.resize(self.size // 2)
        return val
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Remove from empty array")
        self.end = (self.end - 1 + self.size) % self.size
        val = self.arr[self.end]
        self.arr[self.end] = None
        self.count -= 1
        if self.count > 0 and self.count == self.size // 4:
            self.resize(self.size // 2)
        return val
    
    def get_first(self):
        if self.is_empty():
            raise IndexError("Get from empty array")
        return self.arr[self.start]
    
    def get_last(self):
        if self.is_empty():
            raise IndexError("Get from empty array")
        return self.arr[(self.end - 1 + self.size) % self.size]
    
    def is_full(self):
        return self.count == self.size
    
    def is_empty(self):
        return self.count == 0
    
    def size(self): return self.count

    

