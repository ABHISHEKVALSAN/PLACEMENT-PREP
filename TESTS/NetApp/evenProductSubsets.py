def power(x,n):
    print(x,n)
    if n==0:
        return 1
    if n==1:
        return x
    if n%2==1:
        return int(x*power(x,n-1)%(10**9+7))
    return int(((power(x,n/2)%(10**9+7))*(power(x,n/2)**(10**9+7)))%(10**9+7))

n=int(input())
if n%2:
    nodd=n//2 + 1
else:
    nodd=n/2
print(power(2,n)-power(2,nodd))
