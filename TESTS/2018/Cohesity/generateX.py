import math
def solve(x,a,b):
    X=int(2**math.ceil(math.log(x,2)))
    dp=[i*a for i in range(X+1)]
    i=1
    while i<=x:
        dp[i]=min(dp[i-1]+a,dp[i],dp[i+1]+a)
        j=i*2
        if j<=X:
            dp[j]=min(dp[j],dp[i]+b)
            dp[j-1]=min(dp[j-1],dp[j]+a)
        i+=1
    return dp[x]
x=int(input())
a,b=map(int,input().split())
print(solve(x,a,b))
