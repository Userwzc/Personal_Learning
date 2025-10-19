# 哈希表
# 关键概念
# key是唯一的， value可以重复, 类比数组，数组里的每个索引都是唯一的，不可能说有两个相同的索引
# 哈希函数： 把任意产长度的输入(key)转化为固定长度的输出（索引）
# 增删改查方法中都会用到哈希函数来计算索引，因此这个函数的性能很重要
# f: key -> hash(key) -> index  ,输入相同的key,输出也必须要相同,这样才能保证哈希表的正确性
# int hash(K key) {
#     int h = key.hashCode();
#     //保证非负数
#     h = h & 0x7fffffff;
#     //映射到table数组的合法索引
#     return h % table.length;
# }

# 哈希冲突
# 常见解决方法，拉链法和开放寻址法（线性探查法）
# 对应纵向延伸和横向延伸两种思路

 
# 扩容和负载因子（避免哈希表装的太满）
# size/capacity = load factor  ,size 是 key-value对的数量，capacity是哈希表底层数组的容量
# 当哈希表内元素的数量超过负载因子*容量时，就需要扩容，类似于动态数组的扩容

# 重点：key在底层中的分布是随机的，即哈希表中键的遍历顺序是无序的
# key必须是不可变类型（immutable），Python中例如字符串、数字、元组等

# 拉链法实现哈希表
class MyChainingHashMap:

    # 拉链表的节点
    class KVNode:
        def __init__(self, key, val):
            self.key = key
            self.val = val
    
    def __init__(self, init_capacity=4):
        self.size = 0
        # 容量至少为1, hash函数中会用到取模运算，避免除0错误
        self.capacity = max(1, init_capacity)
        self.table = [[] for _ in range(self.capacity)]

    def put(self, key, val):
        if key is None:
            raise ValueError("key is None")
        index = self._hash(key)
        bucket = self.table[index]
        for node in bucket:
            if node.key == key:
                node.val = val
                return
        
        # key不存在，新增
        bucket.append(self.KVNode(key, val))
        self.size += 1

        # 负载因子阈值0.75
        if self.size >= 0.75 * self.capacity:
            self._resize(2 * self.capacity)

    def remove(self, key):
        if key is None:
            raise ValueError("key is not exist")
        index = self._hash(key)
        bucket = self.table[index]
        for node in bucket:
            if node.key == key:
                bucket.remove(node)
                self.size -= 1

                if self.size <= self.capacity / 8:
                    self._resize(max(self.capacity // 4, 1))
                return 
            
    def get(self, key):
        if key is None:
            raise ValueError("key is not exist")
        index = self._hash(key)
        bucket = self.table[index]
        for node in bucket:
            if node.key == key:
                return node.val
        
        return None
    
    def keys(self):
        keys = []
        for bucket in self.table:
            for node in bucket:
                keys.append(node.key)

        return keys
    
    def size(self):
        return self.size
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def _resize(self, new_capacity):
        new_table = MyChainingHashMap(new_capacity)
        for bucket in self.table:
            for node in bucket:
                new_table.put(node.key, node.val)

        self.table = new_table.table
        self.capacity = new_table.capacity
        del new_table

if __name__ == "__main__":
    map = MyChainingHashMap()
    map.put(1, 1)
    map.put(2, 2)
    map.put(3, 3)
    print(map.get(1))  # 1
    print(map.get(2))  # 2

    map.put(1, 100)
    print(map.get(1))  # 100

    map.remove(2)
    print(map.get(2))  # None
    print(map.keys()) # [1, 3]

    map.remove(1)
    map.remove(2)
    map.remove(3)
    print(map.get(1))  # None