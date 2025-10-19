# 线性探查法
# 难点一：需要环形数组技巧
# 难点二：删除节点后，需要重新探查后面的元素，防止断链
# 线性探查法使用得不多，大部分编程语言标准库实现的哈希表都是使用拉链法
# 1.搬移数据的线性探查法
class KVNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyLinearProbingHashMap:

    INIT_CAP = 4
    def __init__(self, cap=INIT_CAP):
        self.table = [None] * cap
        self.size = 0

    def hash(self, key):
        return key % len(self.table)
    
    def put(self, key, val):
        if self.size >= 0.75 * len(self.table):
            self.resize(2 * len(self.table))
        
        index = self.hash(key)
        # 如果index位置不为空，则继续向后找
        while self.table[index] is not None:
            # 如果key已经存在，更新value
            if self.table[index].key == key:
                self.table[index].val = val
                return
            index = (index + 1) % len(self.table)
        # 如果没有找到空位，则扩容
        self.table[index] = KVNode(key, val)
        self.size += 1

    def get(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].val
            index = (index + 1) % len(self.table)
        return None

    def remove(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index] = None
                # 重新探查后面的元素
                next_index = (index + 1) % len(self.table)
                while self.table[next_index] is not None:
                    # 重新计算哈希值
                    new_index = self.hash(self.table[next_index].key)
                    if new_index != next_index:
                        self.table[index] = self.table[next_index]
                        self.table[next_index] = None
                        index = next_index
                    next_index = (next_index + 1) % len(self.table)
                return
            index = (index + 1) % len(self.table)   

    def remove2(self, key):
        if self.size <= len(self.table) // 8:
            self.resize(len(self.table) // 4)

        index = self.findKeyIndex(key)
        if index is None:
            return
        self.table[index] = None
        self.size -= 1
        # 重新插入后续元素，防止断链rehash
        index = (index + 1) % len(self.table)
        while self.table[index] is not None:
            node = self.table[index]
            self.table[index] = None
            self.size -= 1
             # 重新插入
            self.put(node.key,node.val)
            index = (index + 1) % len(self.table)

    def resize(self, new_capacity):
        old_table = self.table
        self.table = [None] * new_capacity
        self.size = 0
        for node in old_table:
            if node is not None:
                self.put(node.key, node.val)

    def findKeyIndex(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index].key == key:
                return index
            index = (index + 1) % len(self.table)

        return index    

# 2.特殊占位符的线性探查法
class MyLinearProbingHashmap2:
    DELETED = KVNode(None, None)
    INIT_CAP = 4
    def __init__(self, init_capacity=INIT_CAP):
        self.table = [None] * init_capacity
        self.size = 0

    def put(self, key ,val):
        if self.size >= 0.75 * len(self.table):
            self.resize(2 * len(self.table))
        index = self.find_key_index(key)
        if index != -1:
            # node = self.table[index]
            # if node is not None:
            #     node.val = val
            #     return 
            self.table[index].val = val
            return

        node = KVNode(key, val)
        # 在table中找一个空位或者占位符进行插入
        index = self.hash(key)
        while self.table[index] is not None and self.table[index] is not type(self).DELETED:
            index = (index + 1) % len(self.table)
        self.table[index] = node
        self.size +=1

    def remove(self,key):
        if self.size < len(self.table) // 8:
            self.resize(max(len(self.table) // 2))
        
        index = self.find_key_index(key)
        if index == -1:
            return
        self.table[index] = type(self).DELETED
        self.size -= 1

    def get(self, key):
        index = self.find_key_index(key)
        if index == -1:
            return None
        return self.table[index].val
    
    def find_key_index(self, key):
        # 因为删除元素时，只是标记为DELETED，并不是真的删除，所以table可能会被填满，导致死循环
        # step 用来记录查找的步数，防止死循环
        step = 0
        index = self.hash(key)
        while self.table[index] is not None:
            step += 1
            # 防止死循环
            if step > len(self.table):
                # 这里可以触发一次resize，把标记为删除的占位符清理
                self.resize(len(self.table))
                return -1
            if self.table[index] is type(self).DELETED:
                index = (index + 1) % len(self.table)
                continue
            if self.table[index].key == key:
                return index
            index = (index + 1) % len(self.table)
        return -1  # key不存在或者已经被删除
    
    def hash(self,key):
        return key % len(self.table)
    
    def resize(self,cap):
        old_table = self.table
        self.table = [None] * cap
        self.size = 0
        for node in old_table:
            if node is not type(self).DELETED and node is not None:
                self.put(node.key,node.val)
        

if __name__ == "__main__":
    map1 = MyLinearProbingHashMap(10)
    map1.put(1, 1)
    map1.put(2,2)
    map1.put(10,10)
    map1.put(20,20)
    map1.put(30,30)
    map1.put(3,3)
    print(map1.get(1))
    print(map1.get(2))
    print(map1.get(20))
    
    map1.put(1, 100)
    print(map1.get(1))

    map1.remove2(20)
    print(map1.get(20))
    print(map1.get(30))

    map2 = MyLinearProbingHashmap2(10)
    map2.put(1,1)
    map2.put(2,2)
    map2.put(10,10)
    map2.put(20,20)
    map2.put(30,30)
    map2.put(3,3)
    print(map2.get(1))
    print(map2.get(2))
    print(map2.get(20))
    map2.put(1,100)
    print(map2.get(1))
    map2.remove(20)
    print(map2.get(20))
    print(map2.get(30))
