# 线性探查法
# 难点一：需要环形数组技巧
# 难点二：删除节点后，需要重新探查后面的元素，防止断链
# 线性探查法使用得不多，大部分编程语言标准库实现的哈希表都是使用拉链法
class KVNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyLinearProbingHashMap:
    def __init__(self):
        self.table = [None] * 10
    
    def hash(self, key):
        return key % len(self.table)
    
    def put(self, key, val):
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

