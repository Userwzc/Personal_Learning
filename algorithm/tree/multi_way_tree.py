# 多叉树的递归/层序遍历
# 多叉树结构就是二叉树结构的延伸，二叉树是特殊的多叉树
# 多叉树的遍历就是二叉树遍历的延伸
# 森林是指多个多叉树的集合，单独一棵多叉树是一个特殊的森林
class Node:
    def __init__(self, val:int):
        self.val = val
        self.children = []  # 多叉树的孩子节点是一个列表

# N叉树的递归遍历框架
def traverse_n_ary_tree(root):
    if root is None:
        return
    # 前序位置
    for child in root.children:
        traverse_n_ary_tree(child)   # 多叉树可能有多个节点，所谓的中序位置也就没什么意义了
    # 后序位置

# N叉树的层序遍历
# 写法一
from collections import deque
def level_order_n_ary_tree_1(root):
    if root is None:
        return 
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        for child in node.children:
            queue.append(child)

# 写法二,记录节点深度
def level_order_n_ary_tree_2(root):
    if root is None:
        return 
    queue = deque([root])
    depth = 1
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            print(f"depth = {depth}, val = {node.val}")
            for child in node.children:
                queue.append(child)
        depth += 1

# 写法三，适配不同权重边
class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth

def level_order_n_ary_tree_3(root):
    if root is None:
        return 
    queue = deque([State(root, 1)])
    while queue:
        state = queue.popleft()
        node = state.node
        depth = state.depth
        print(f"depth = {depth}, val = {node.val}")
        for child in node.children:
            queue.append(State(child, depth + 1))