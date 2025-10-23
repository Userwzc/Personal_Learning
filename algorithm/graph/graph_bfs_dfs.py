# 图结构的DFS/BFS遍历
# 图的遍历就是多叉树遍历的延伸，主要遍历方式还是深度优先搜索(DFS)和广度优先搜索(BFS)
# 唯一的区别是，树结构中不存在环，而图结构中可能存在环，所以我们需要标记遍历过的节点，避免遍历函数在环中死循环
# 由于图结构的复杂性，可以细分为遍历图的[节点]、[边]、[路径]三种场景，每种场景的代码实现略有不同
# 遍历图的[节点]和[边]时，需要visited数组在前序位置做标记，避免重复遍历；遍历图的[路径]时，需要onPath数组在前序位置标记节点，在后序位置撤销标记


# 多叉树节点
class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children is not None else []

# 多叉树的遍历框架
def traverse(root):
    if root is None:
        return 
    # 前序位置
    print(root.val)
    for child in root.children:
        traverse(child)
    # 后序位置

# 图节点
class Vertex:
    def __init__(self, id, neighbors=None):
        self.id = id
        self.neighbors = neighbors if neighbors is not None else [] 

# 图的遍历框架
# 需要一个visited数组记录被遍历过的节点
# 避免走回头路陷入死循环
def traverse_graph(s: Vertex, visited: list[bool]):
    if s is None:
        return
    if visited[s.id]:
        return
    # 前序位置
    visited[s.id] = True
    print(f"visit {s.id}")
    for neighbor in s.neighbors:
        traverse_graph(neighbor, visited)
    # 后序位置

# 基于graph_structure.py中的图结构的遍历框架：
def traverse_graph_structure(graph, s: int, visited: list[bool]):
    if graph is None or s < 0 or s >= len(graph):
        return
    if visited[s]:
        return
    # 前序位置
    visited[s] = True
    print(f"visit {s}")
    for edge in graph.neighbors(s):
        traverse_graph_structure(graph, edge.to, visited)
    # 后序位置

# 由于visited数组的剪枝作用，这个遍历函数会遍历一次图中所有的节点，并尝试遍历一次所有边，所以算法的时间复杂度是O(V+E)

# 遍历所有边（二维visited数组）
# 对于图结构，遍历所有边的场景其实并不多见，主要是计算欧拉路径时会用到
# 上面遍历所有节点用一个一维的visited数组记录已经访问过的节点，确保每个节点只被遍历一次；那么最简单的实现思想就是用一个二维的visited数组来记录遍历过的边
# visited[u][v] 表示边u->v是否被遍历过,从而确保每条边只被遍历一次 
def traverse_edges(s, visited):
    # base case
    if s is None:
        return
    for neighbor in s.neighbors:
        # 如果边已经被遍历过，则跳过
        if visited[s.id][neighbor.id]:
            continue
        # 标记并访问边
        visited[s.id][neighbor.id] = True
        print(f"visit edge: {s.id} -> {neighbor.id}")
        traverse_edges(neighbor, visited)
    # 由于一条边由两个节点构成，所以我们需要把前序位置的相关代码放到 for 循环内部。

# 基于graph_structure.py中的图结构的遍历所有边框架：
def traverse_edges_graph_structure(graph, s: int, visited: list[list[bool]]):
    if graph is None or s < 0 or s >= len(graph):
        return
    for edge in graph.neighbors(s):
        # 如果边已经被遍历过，则跳过
        if visited[s][edge.to]:
            continue
        # 标记并访问边
        visited[s][edge.to] = True
        print(f"visit edge: {s} -> {edge.to}")
        traverse_edges_graph_structure(graph, edge.to, visited)
# 显然使用二维visited数组并不是一个高效的实现方式,因为需要创建二维visited数组，这个算法的时间复杂度为O(E+V^2)，空间复杂度为O(V^2)