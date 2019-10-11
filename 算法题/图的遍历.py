# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:53:00 2019

@author: yllzxzyq
"""

class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class graph:

    def __init__(self,graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict
# Check for the visisted and unvisited nodes

import collections
def bfs(graph, start_node):
# Track the visited and unvisited nodes using queue
    seen, queue = {start_node}, collections.deque([start_node])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
    return order

def dfs(graph,start):
    if not graph:
        return
    visited,stack = set(),[start]
    order = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return order

graph_dict = { "a" : {"b", "c"},
                "b" : {"a", "d"},
                "c" : {"a", "d"},
                "d" : {"e"},
                "e" : {"a"}
                }

print(dfs(graph_dict,'a'))




