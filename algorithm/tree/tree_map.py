# TreeMap底层把键值对存储在一颗二叉搜索树的节点里面

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.left = None
        self.right = None

# 哈希表很实用，但是它确实没办法很好地处理键之间的大小关系，前面用链表加强哈希表中实现的LinkedHashMap也只是
# 做到按[插入顺序]排列哈希表中的键，依然做不到按[大小顺序]排列

# 二叉搜索树(BST)的性能取决于树的高度，树的高度取决于树的平衡性
# 因此在实际应用中，TreeMap需要自动维护树的平衡，避免出现性能退化

# 红黑树是自平衡的二叉搜索树，它的树高在任何时候都能保持在O(logN)(完美平衡),可以保证增删查改的时间复杂度都是O(logN)

