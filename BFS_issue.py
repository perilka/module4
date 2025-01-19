from collections import deque

class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

class Graph:
    def __init__(self, root):
        self._root = root
        self.dfs_list = [self._root]
        self.bfs_list = []

    def to_visit_dfs(self, node: Node) -> list[Node]:
        for neighbor in node.outbound:
            if neighbor not in self.dfs_list:
                self.dfs_list.append(neighbor)
                self.to_visit_dfs(neighbor)
        return self.dfs_list

    def dfs(self):
        return [str(node) for node in self.to_visit_dfs(self._root)]

    def to_visit_bfs(self, node: Node) -> list[Node]:
        queue = deque()
        queue.append(node)
        self.bfs_list.append(node)
        while queue:
            vertex = queue.popleft()
            for neighbor in vertex.outbound:
                if neighbor not in self.bfs_list:
                    queue.append(neighbor)
                    self.bfs_list.append(neighbor)
        return self.bfs_list

    def bfs(self):
        return [str(node) for node in self.to_visit_bfs(self._root)]




a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)

print(f'Обход в глубину: {g.dfs()}')
print(f'Обход в ширину: {g.bfs()}')
print()


a = Node('a')
b = Node('b')
c = Node('c')
a.point_to(b)
b.point_to(c)

g = Graph(a)

print(f'Обход в глубину: {g.dfs()}')
print(f'Обход в ширину: {g.bfs()}')
print()


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
b.point_to(f)
c.point_to(e)

g = Graph(a)

print(f'Обход в глубину: {g.dfs()}')
print(f'Обход в ширину: {g.bfs()}')
print()


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

g = Graph(a)

print(f'Обход в глубину: {g.dfs()}')
print(f'Обход в ширину: {g.bfs()}')
print()