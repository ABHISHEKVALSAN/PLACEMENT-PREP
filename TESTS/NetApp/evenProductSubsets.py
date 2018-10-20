def power(x,n):
    global mod
    print(x,n)
    if n==0:
        return 1
    if n==1:
        return x
    if n%2==1:
        return int(x*power(x,n-1)%mod)
    return int(((power(x,n/2)%mod) * (power(x,n/2)%mod))%mod)
mod=10**9+7
n=int(input())
if n%2:
    nodd=n//2 + 1
else:
    nodd=n/2
print(power(2,n)-power(2,nodd))
