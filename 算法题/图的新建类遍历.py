# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:54:32 2019

@author: yllzxzyq
"""

class ComponentsCounter(object):
    def __init__(self,aGraph):
        self.graph = aGraph
        self.result = 0 #store the number of component
        self.calc()

    def calc(self):
        for vertex in self.graph:
            vertex.setVisited(False) #let all the vertex being not visited
        for vertex in self.graph:
            if not vertex.getVisited(): #using dfs scan all the vertex that is not visited
                self._dfs(vertex,self.graph.getCCount())
                self.graph.setCCount(self.graph.getCCount() + 1)
                self.result += 1 #done,we need to plus 1

    def _dfs(self,startVertex,ccount):
        startVertex.setCCID(ccount) 
        #we can use id to check whether the two vertices was the same component or not.
        startVertex.setVisited(True)
        for nextVertex in startVertex.getConnections():
            if not nextVertex.getVisited():
                self._dfs(nextVertex,ccount)

    def getResult(self):
        return self.result