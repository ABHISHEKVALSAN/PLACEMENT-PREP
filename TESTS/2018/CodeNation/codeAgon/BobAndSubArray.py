n=int(raw_input())
arr=map(int,raw_input().split())
mx=max(arr)
ml=len(bin(mx)[2:])
l=[]
for e in arr:
    temp=bin(e)[2:]
    temp="0"*(ml-len(temp))+temp
    sl=map(int,list(temp))
    l.append(sl)
nl=map(list,zip(*l))
ss=0
#print nl
p=ml-1
for l in nl:
    s=0
    temp=0
    for i  in range(n-1,-1,-1):
        if l[i]==1:
            temp=n-i
        s+=temp
    #print l,s
    ss+=(2**p)*s
    p-=1
print ss
