class graph:
    def __init__(self,V):
        self.V=V
        self.adj=[]
        for i in range(V):
            self.adj.append(set())
    def addEdge(self,u,v):
        self.adj[v-1].add(u)
        self.adj[u-1].add(v)

def solve(n,edgeList,host):
    g=graph(n)
    visited=[]
    for i in range(n):
        visited.append('False')
    for i in edgeList:
        g.addEdge(i[0],i[1])
    visited[host-1]='True'
    queue=[]
    for ele in g.adj[host-1]:
        if visited[ele-1]=='False':
            queue.append(ele)
    queue.sort()
    ans=[]
    while queue!=[]:
        ans+=queue
        for q in queue:
            visited[q-1]='True'
        temp=[]
        for q in queue:
            for ele in g.adj[q-1]:
                if visited[ele-1]=='False':
                    temp.append(ele)
        temp.sort()
        queue=temp
    return ans

def main():
    nv,ne=map(int,raw_input().split())
    edgeList=[]
    for i in range(ne):
        u,v=map(int,raw_input().split())
        edgeList.append([u,v])
    host=int(raw_input())
    print solve(nv,edgeList,host)
if __name__=="__main__":
    main()
