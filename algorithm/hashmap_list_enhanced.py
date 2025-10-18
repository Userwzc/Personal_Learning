# 用链表加强哈希表
class MyLinkedHashMap:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = dict()

    def get(self, key):
        if key not in self.map:
            return None
        return self.map[key].val
    
    def put(self, key, val):
        if key not in self.map:
            new_node = self.Node(key, val)
            self.add_last_node(new_node)
            self.map[key] = new_node
            return 
        self.map[key].val = val

    def remove(self, key):
        if key not in self.map:
            return 
        node = self.map[key]
        self.remove_node(node)
        del self.map[key]

    def contains(self, key):
        return key in self.map
    
    def keys(self):
        keys_list = []
        current = self.head.next
        while current != self.tail:
            keys_list.append(current.key)
            current = current.next
        return keys_list

    def add_last_node(self, node):
        last = self.tail.prev
        last.next = node 
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del node

if __name__ == "__main__":
    map1 = MyLinkedHashMap()
    map1.put("a", 1)
    map1.put("b", 2)
    map1.put("c", 3)
    map1.put("d", 4)
    map1.put("e", 5)

    print(map1.keys())
    map1.remove("c")
    print(map1.keys())
