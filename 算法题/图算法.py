class graph:
    def __init__(self,Vertex = None, Edge = None):
        self.Vertex = []
        self.Edge = dict()

    def add_Vertex(self,v):
        self.Vertex.append(v)

    def add_Edge(self,v1,v2):
        if v1 in self.Edge:
            self.Edge[v1].add(v2)
        else:
            self.Edge[v1] = {v2}
    def delete_Vertex(self,v):
        self.Vertex.pop(v)

    def delete_edge(self,v1,v2):
        self.Edge[v1].pop(v2)

g = graph()
for i in range(10):
    g.add_Vertex(i)
    g.add_Edge(i,i-1)
print(g.Vertex)
print(g.Edge)