class GraphNode:
    def __init__(self, data):
        self.parent = None
        self.dist = float('+inf')
        self.visited = False
        self.adjList = []

    def connect(self, other):
        if other is None:
            return
        if other not in self.adjList:
            self.adjList.append(other)
        #

    def get_neigh(self):
        return self.adjList()

    def __str__(self):
        neigh_str = ",".join(self.adjList)
        return "{}->{}".format(self.data, neigh_str)


class Graph:

    def __init__(self):
        self.roots = []

    def add_node(self, node):
        if node is None:
            return
        if node not in self.roots:
            self.roots.append(node)

    def add_edge(self, nd1, nd2):
        if nd1 is None or nd2 is None:
            return
        nd1.connect(nd2)
        nd2.connect(nd1)


    def organize(self):
        new_roots = []
        for r in self.roots:
            if not r.visited:
                new_roots.append(r)
            self.bfs(r)
        # end of for
        self.roots = new_roots

    def bfs(self, root):
        root.parent = None
        root.dist = 0
        root.visited = True
        queue = [root]
        while not queue:
            cur_elm = queue[-1]
            queue.remove(cur_elm)
            for v in cur_elm.get_neigh():
                if not v.visited:
                    v.visted = True
                    v.parent = cur_elm
                    v.dist = cur_elm.dist+1
                # end of if
                queue.append(v)
            # end of for
        # end of while

# end of class Graph
