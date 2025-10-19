# 二叉树遍历只有递归遍历和层序遍历两种，再无其它。
# 递归遍历可以衍生出DFS算法，而层序遍历可以衍生出BFS算法。
# 递归遍历二叉树节点的顺序是固定的，但是有三个关键位置，在不同位置插入代码，会产生不同的效果
# 层序遍历二叉树节点的顺序也是固定的，但是有三种不同的写法，对应不同的场景

# 基本的二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树的递归遍历框架
def traverse(root):
    if root is None:
        return 
    # 前序位置
    traverse(root.left)
    # 中序位置
    traverse(root.right)
    # 后序位置

# BST的中序遍历顺序是有序的

# 二叉树的层序遍历
# 顾名思义，就是一层一层地遍历
# 写法一
from collections import deque
def level_order_1(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
# 这种写法的优势是简单，但是缺点是无法知道当前位置在第几层

# 写法二
def level_order_2(root):
    if root is None:
        return 
    queue = deque([root])
    depth = 1
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            print(f"depth = {depth}, val = {node.val}")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        depth += 1
# 这种写法可以知道当前位置在第几层

# 写法三
# 解决每个树枝的路径权重问题,让每个节点自己负责维护自己的路径权重和
class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth


def level_order_3(root):
    if root is None:
        return
    queue = deque([State(root, 1)]) # 初始时，根节点的深度是1
    while queue:
        state = queue.popleft()
        print(f"depth = {state.depth}, val = {state.node.val}")
        if state.node.left is not None:
            queue.append(State(state.node.left, state.depth + 1))
        if state.node.right is not None:
            queue.append(State(state.node.right, state.depth + 1))
