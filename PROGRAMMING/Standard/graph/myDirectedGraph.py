from collections import defaultdict

import random
# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self,V):
        self.V              =   V
        self.E              =   0
        self.vertexList     =   range(V)
        self.adjList        =   []
        self.adjMat         =   []
        self.edgeList       =   []
        for i in range(V):
            self.adjList.append([])
    def makeAdjMat(self,V):
        adjMat=[]
        for i in range(V):
            adjMat.append([])
            for j in range(V):
                adjMat[i].append(float("inf")*-1)
        for i in range(V):
            adjMat[i][i]=0
        return adjMat
    def addEdge(self,u,v,w=1):
        self.adjList[u].append(v)
        self.edgeList.append([u,v,w])
    def createGraph(self,filename,directed):
        f=open(filename,"r")
        for edge in f:
            e=map(int,str(edge[:-1]).split(" "))
            self.addEdge(e[0],e[1],e[2])
            if not directed:
                self.addEdge(e[1],e[0],e[2])
    def getAdjEdges(self,vertex):
        l=[]
        edgeList=self.edgeList
        for edge in edgeList:
            if vertex in edge[:-1]:
                l.append(edge)
        return l
    def getAdjList(self):
        return self.adjList
    def getEdgeList(self):
        return self.edgeList
    def getRandomVertex(self):
        return random.choice(self.vertexList)
    def DFS(self,v):
        def DFSUtil(self,v,visited):
            visited[v]= True
            print v,
            for i in self.adjList[v]:
                if visited[i] == False:
                    self.DFSUtil(i, visited)
        visited = [False]*self.V
        self.DFSUtil(v,visited)
    def BFS(self,v):
        def BFSUtil(self,v,visited,queue):
            visited[v]=True
            print v,
            for i in self.adjList[v]:
                if visited[i]==False:
                    visited[i]=True
                    queue.append(i)
            if queue==[]:
                return
            vertex=queue.pop(0)
            self.BFSUtil(vertex,visited,queue)
        visited = [False]*self.V
        queue   = []
        self.BFSUtil(v,visited,queue)
    def Kruskals(self):
        pi={}
        rank={}
        for i in range(self.V):
            pi[i]=i
            rank[i]=0
        def find(x):
            while x!=pi[x]:
                x=pi[x]
            return x
        def union(x,y):
            rx=find(x)
            ry=find(y)
            if rx==ry:
                return
            if rank[rx]>rank[ry]:
                pi[ry]=rx
            else:
                pi[rx]=ry
                if rank[rx]==rank[ry]:
                    rank[ry]=rank[ry]+1

        edgeList=self.getEdgeList()
        edgeList.sort(key = lambda x: x[2])
        visited=[]
        for i in range(self.V):
            visited.append('False')
        MST=[]
        for edge in edgeList:
            if find(edge[0])!=find(edge[1]):
                MST.append(edge)
                union(edge[0],edge[1])
        return MST
    def Prims(self):
        cost={}
        prev={}
        for v in range(self.V):
            cost[v]=float("inf")
            prev[v]=-1
        v=self.getRandomVertex()
        cost[v]=0
        H=cost
        while H!=[]:
            v=min(H,key=lambda x: H[x])
            w=H[v]
            del H[v]
            edges=self.getAdjEdges(v)
            for edge in edges:
                z=edge[0]+edge[1]-v
                w=edge[2]
                if cost[z]>w:
                    cost[z]=w
                    prev[z]=v

        return prev
def main():
    g = Graph(5)
    directed="False"
    g.createGraph("graph_3",directed)
    prev=g.Prims()
    print prev
if __name__=="__main__":
    main()
