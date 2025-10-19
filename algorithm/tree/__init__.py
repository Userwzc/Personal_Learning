"""二叉树数据结构子包。"""

# 满二叉树  Perfect Binary Tree
# 完全二叉树  Complete Binary Tree：二叉树的每一层的节点都紧凑靠左排列，且除了最后一层，其他每层都必须是满的
# 完全二叉树的左右子树中，至少有一颗是满二叉树

# 二叉搜索树  Binary Search Tree
# 对于二叉搜索树中的每个节点 node，左子树上所有节点的值均小于 node 的值，右子树上所有节点的值均大于 node 的值
# “左小右大”

# 高度平衡二叉树  Height-Balanced Binary Tree
# 对于二叉树中的每个节点，其左右子树的高度差不超过 1
# 假设高度平衡二叉树共有N个节点，则其高度h与节点数N满足关系：h=O(logN)
# 增删查改效率高

# 自平衡二叉树  Self-Balanced Binary Tree
# 在增删二叉树节点时对树的结构进行一些调整，使其保持高度平衡
# 有多种实现方式，如AVL树、红黑树等