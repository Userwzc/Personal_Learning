# 图结构的通用代码实现
# 图结构就是多叉树结构的延伸，我们一般用邻接表、邻接矩阵等方式来存储图.


# 有向加权图(邻接表实现)
class WeightedDigraph:
    # 存储相邻节点及边的权重
    class Edge:
        def __init__(self, to, weight):
            self.to = to
            self.weight = weight

    def __init__(self, n : int):
        # 简单起见，传入节点总数
        # 可以设置为动态增加节点 dict <int, list<Edge>>
        self.graph = [[] for _ in range(n)]

    # 增，添加一条带权重的有向边，复杂度O(1)
    def addEdge(self, from_: int , to: int, weight: int):
        self.graph[from_].append(self.Edge(to, weight))
    
    # 删，删除一条有向边，复杂度O(V)
    def removeEdge(self, from_: int, to: int):
        self.graph[from_] = [edge for edge in self.graph[from_] if edge.to != to]

    # 查，判断两个节点是否相邻，复杂度O(V)
    def hasEdge(self, from_: int, to: int) -> bool:
        for edge in self.graph[from_]:
            if edge.to == to:
                return True
        return False
    
    # 查，返回一条边的权重，复杂度O(V)
    def weight(self, from_: int, to: int) -> int:
        for e in self.graph[from_]:
            if e.to == to:
                return e.weight
        raise ValueError("No such edge")
    
    # 上面的 hasEdge、removeEdge、weight 方法遍历 List 的行为是可以优化的
    # 比如用 Map<Integer, Map<Integer, Integer>> 存储邻接表
    # 这样就可以避免遍历 List，复杂度就能降到 O(1)    

    def neighbors(self, v: int):
        return self.graph[v]

# 有向加权图(邻接矩阵实现)
class WeightedDigraphMatrix:
    class Edge:
        def __init__(self, to, weight):
            self.to = to
            self.weight = weight

    def __init__(self, n):
        self.matrix = [[0]* n for _ in range(n)]

    # 增，添加一条带权重的有向边，复杂度O(1)
    def addEdge(self, from_: int , to: int, weight: int):
        self.matrix[from_][to] = weight
    
    # 删，删除一条有向边，复杂度O(1)
    def removeEdge(self, from_: int, to: int):
        self.matrix[from_][to] = 0

    # 查，判断两个节点是否相邻，复杂度O(1)
    def hasEdge(self, from_: int, to: int) -> bool:
        return self.matrix[from_][to] != 0
    
    # 查，返回一条边的权重，复杂度O(1)
    def weight(self, from_: int, to: int):
        return self.matrix[from_][to]
    
    # 查，返回节点v的所有邻居节点，复杂度O(V)
    def neighbors(self, v):
        return [self.Edge(to, self.matrix[v][to]) for to in range(len(self.matrix)) if self.matrix[v][to] != 0]

# 有向无权图(邻接表/邻接矩阵实现)，可以参考上面的加权图实现，只需将权重参数设置为1即可。

# 无向加权图(邻接表/邻接矩阵实现),无相加权图等同于双向的有向加权图，直接复用上面的代码即可。
class WeightedUndigraph:
    def __init__(self,n):
        self.graph = WeightedDigraph(n)

    def addEdge(self, from_: int , to: int, weight: int):
        self.graph.addEdge(from_, to, weight)
        self.graph.addEdge(to, from_, weight)

    def removeEdge(self, from_: int, to: int):
        self.graph.removeEdge(from_, to)
        self.graph.removeEdge(to, from_)

    def hasEdge(self, from_: int, to: int) -> bool:
        return self.graph.hasEdge(from_, to)
    
    def weight(self, from_: int, to: int):
        return self.graph.weight(from_, to)
    
    def neighbors(self, v: int):
        return self.graph.neighbors(v)
    
# 无向无权图(邻接表/邻接矩阵实现)，可以参考上面的加权图实现，只需将权重参数设置为1即可。

if __name__ == "__main__":
    # graph = WeightedDigraphMatrix(3)
    # graph.addEdge(0,1,1)
    # graph.addEdge(1,2,2)
    # graph.addEdge(2,0,3)
    # graph.addEdge(2,1,4)

    # print(graph.hasEdge(0,1))  # True
    # print(graph.hasEdge(1,0))  # False

    # for edge in graph.neighbors(2):
    #     print(f"{2} -> {edge.to} with weight {edge.weight}")

    # graph.removeEdge(0,1)
    # print(graph.hasEdge(0,1))  # False

    graph = WeightedUndigraph(3)
    graph.addEdge(0, 1, 1)
    graph.addEdge(2, 0, 3)
    graph.addEdge(2, 1, 4)

    print(graph.hasEdge(0, 1))  # true
    print(graph.hasEdge(1, 0))  # true

    for edge in graph.neighbors(2):
        print(f"{2} <-> {edge.to}, weight: {edge.weight}")
    # 2 <-> 0, weight: 3
    # 2 <-> 1, weight: 4

    graph.removeEdge(0, 1)
    print(graph.hasEdge(0, 1))  # false
    print(graph.hasEdge(1, 0))  # false

    