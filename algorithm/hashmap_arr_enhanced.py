# 用数组加强哈希表
import random
class Node:
    def __init__(self, key , val):
        self.key = key
        self.val = val

class MyArrHashMap:
    def __init__(self):
        # 存储key 和 key在arr中的索引
        self.map = {}
        # 存储key-val节点的数组
        self.arr = []
    
    def get(self, key):
        if key not in self.map:
            return None
        index = self.map[key]
        return self.arr[index].val
    
    def put(self, key, val):
        if self.contains(key):
            index = self.map[key]
            self.arr[index].val = val
            return
        new_node = Node(key, val)
        self.arr.append(new_node)
        self.map[key] = len(self.arr) - 1

    def remove(self, key):
        if not self.contains(key):
            return 
        index = self.map[key]
        # 将要删除的节点和最后一个节点交换位置，然后删除最后一个节点
        self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
        self.arr.pop()
        # 更新map中最后一个节点的索引
        self.map[self.arr[index].key] = index
        # 删除key
        del self.map[key]

    def random_key(self):
        if not self.arr:
            return None
        n = len(self.arr)
        rand_index = random.randint(0, n - 1)
        return self.arr[rand_index].key
    
    def contains(self, key):
        return key in self.map
    
    def size(self):
        return len(self.map)
    

if __name__ == "__main__":
    map = MyArrHashMap()
    map.put(1, 1)
    map.put(2, 2)
    map.put(3, 3)
    map.put(4, 4)
    map.put(5, 5)

    print(map.get(1)) # 1
    print(map.random_key())

    map.remove(4)
    print(map.random_key())
    print(map.random_key())