# 哈希集合
# 哈希表的键，其实就是哈希集合
# 哈希集合的主要使用场景是去重，因为它的特性是不会出现重复元素，可以在O(1)时间增删元素，可以在O(1)的时间判断一个元素是否存在
class MyHashSet:
    def __init__(self):
        # 底层字典，用于存储哈希集合的元素
        self.map = {} 
    
    def add(self, key):
        # 向哈希表集合添加一个键值对，用True作为占位符
        self.map[key] = True

    def remove(self, key):
        # 从哈希表集合中删除一个键值对
        if key in self.map:
            del self.map[key]

    def contains(self, key):
        # 检查哈希表集合中是否存在指定的键
        return key in self.map
    
    def size(self):
        # 获取哈希表集合的大小
        return len(self.map)