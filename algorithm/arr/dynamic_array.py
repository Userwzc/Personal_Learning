class DynamicArray:
    def __init__(self, capacity=None):
        self.size = 0
        self.array = [None] * capacity if capacity else 1
    
        
    def append(self, value):
        cap = len(self.array)
        if self.size == cap:
            self._resize(2 * cap)
        self.array[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

        
    def insert(self, index, value):
        self._check_position(index)

        cap = len(self.array)
        if self.size == cap:
            self._resize(2 * cap)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1
        
    def remove(self, index):
        self._check_element(index)
        
        value = self.array[index]
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        
        cap = len(self.array)
        if self.size == cap // 4:
            self._resize(cap // 2)
    
        return value
    
    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty array")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1

        cap = len(self.array)
        if self.size == cap // 4:
            self._resize(cap // 2)
        return value
    
    def get(self, index):
        self._check_element(index)
        return self.array[index]
    
    def set(self, index, value):
        self._check_element(index)
        old_value = self.array[index]
        self.array[index] = value
        return old_value
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def _is_element(self, index):
        return 0 <= index < self.size
    
    def _is_position(self, index):
        return 0 <= index <= self.size
    
    def _check_element(self, index):
        if not self._is_element(index):
            raise IndexError(f"Index {index} out of Size {self.size}")

    def _check_position(self, index):
        if not self._is_position(index):
            raise IndexError(f"Index {index} out of bounds")

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"
    
    
if __name__ == "__main__":
    
    arr = DynamicArray(capacity=3)
    for i in range(1,6):
        arr.append(i)
        
    arr.remove(3)
    arr.insert(1,9)
    arr.insert(0,100)
    val = arr.pop()
    
    for i in range(arr.get_size()):
        print(arr.get(i))