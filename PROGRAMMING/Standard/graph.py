
N=100;
class Graph:
    def __init__(self,V):
        self.V=V
        self.vertices=set()
        self.adj=[]
        for i in range(V):
            self.adj.append([])
    def addEdge(self,v,w):
        self.adj[v].append(w)
        self.vertices.add(v)
        self.vertices.add(w)
    def getVertices(self):
        return self.vertices
def DFSUtil(g,vertex, visited, stack):
    visited.add(vertex)
    for v in g.adj[vertex]:
        if v in visited:
            continue
        visited,stack=DFSUtil(g,v, visited, stack)
    stack=list(stack)
    stack=[vertex]+stack
    return visited,stack
def DFSUtilForReverseGraph(rg,vertex, visited, s):
    visited.add(vertex)
    s.add(vertex)
    for v in rg.adj[vertex]:
        if v in visited:
            continue
        visited,s=DFSUtil(g,v, visited, s)
    return visited,s
def scc(g,rg):
    stack=[]
    visited=set()
    vertices=g.getVertices()
    for vertex in vertices:
        if vertex in visited:
            continue
        visited,stack=DFSUtil(g,vertex, visited, stack)
    visited=set()
    result=[]
    while stack!=[]:
        vertex=stack[0]
        stack=stack[1:]
        if vertex in visited:
            continue
        s=set()
        visited,s=DFSUtilForReverseGraph(rg,vertex, visited, s)
        result.append(list(s))
    return result
if __name__=="__main__":
    E=[[0,1],[1,2],[2,3],[3,2],[2,1]]
    vertices=4
    g=Graph(vertices)
    rg=Graph(vertices)
    for i in E:
        g.addEdge(i[0],i[1])
        rg.addEdge(i[1],i[0])
    result=scc(g,rg)
    for i in result:
        print i
