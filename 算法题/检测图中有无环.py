class graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_edges(self, edges):
        for i in edges:
            if i[1] not in self.edges:
                self.edges[i[1]] = {i[0]}
            else:
                self.edges[i[1]].add(i[0])
            for j in i:
                if j not in self.nodes:
                    self.nodes.add(j)

class Solution(object):
    def canFinish_DFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        g = graph()
        g.add_edges(prerequisites)
        tag = {}
        node = list(g.nodes)
        for i in node:
            tag[i] = 0

        def dfs(edges, start, tag):
            if tag[start] == -1: return True
            if tag[start] == 1: return False
            tag[start] = 1
            if start in edges:
                for n in edges[start]:
                    if not dfs(edges, n, tag): return False
            tag[start] = -1
            return True

        for i in node:
            if not dfs(g.edges, i, tag): return False
        return True
    def canFinish_BFS(self,numCourses, prerequisites):
        from collections import deque
        if not prerequisites:
            return True
        g = graph()
        g.add_edges(prerequisites)
        node = list(g.nodes)
        n = len(node)
        in_degree = {}
        for i in node:
            in_degree[i] = 0
        for i in g.edges.values():
            for j in node:
                if j in i:
                    in_degree[j] += 1
        stack = deque()
        for i in in_degree:
            if in_degree[i] == 0:
                stack.append(i)
        while stack:
            vertex = stack.popleft()
            n -= 1
            if vertex in g.edges:
                for j in g.edges[vertex]:
                    in_degree[j] -= 1
                    if in_degree[j] == 0:
                        stack.append(j)
        return not n




numCourses = 3
prerequisites = [[1,0],[2,1]]
s = Solution()
print(s.canFinish_BFS(numCourses, prerequisites))
